document.addEventListener("DOMContentLoaded", function () {
  function toggleSpinner(buttonId, spinnerClass, textClass) {
    const button = document.getElementById(buttonId);
    const spinner = document.querySelector(`.${spinnerClass}`);
    const textElement = document.querySelector(`.${textClass}`);

    if (button) {
      button.addEventListener("click", function () {
        if (textElement) textElement.style.display = "none";
        if (spinner) {
          spinner.classList.remove("hidden");
          spinner.style.display = "inline-block";
        }
        setTimeout(function () {
          if (textElement) textElement.style.display = "block";
          if (spinner) {
            spinner.classList.add("hidden");
            spinner.style.display = "none";
          }
        }, 6000);
      });
    }
  }

  toggleSpinner("see-more", "show-more", "see-more");
  toggleSpinner("filter-spinner", "spinner-more", "filter-text");

  const modalButton = document.querySelector(".modal-button");
  const modal = document.querySelector("#errorModal");
  if (modalButton && modal) {
    modalButton.addEventListener("click", function () {
      const modalSpinner = modal.querySelector(".spinner-border");
      const modalActionButton = modal.querySelector(".btn-info");
      if (modalActionButton && modalSpinner) {
        modalActionButton.addEventListener("click", function () {
          modalSpinner.classList.remove("hidden");
        });
      }
    });
  }

  const seeMoreButton = document.getElementById("see-more");
  const protocolsList = document.getElementById("protocols-list");

  if (seeMoreButton && protocolsList) {
    seeMoreButton.addEventListener("click", function () {
      const nextPage = seeMoreButton.getAttribute("data-next-page");
      if (!nextPage) return;

      const url = `?page=${nextPage}`;
      fetch(url)
        .then((response) => response.text())
        .then((data) => {
          const parser = new DOMParser();
          const html = parser.parseFromString(data, "text/html");
          const newProtocols = html.querySelector("#protocols-list")?.innerHTML;
          if (newProtocols) protocolsList.innerHTML += newProtocols;
          const newNextPage = html
            .querySelector("#see-more")
            ?.getAttribute("data-next-page");
          if (newNextPage) {
            seeMoreButton.setAttribute("data-next-page", newNextPage);
          } else {
            seeMoreButton.remove();
          }
        })
        .catch((err) => console.error("Failed to fetch protocols:", err));
    });
  }
});
