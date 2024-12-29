$(document).ready(function () {
  $(".errorcode").click(function () {
    var errortitle = $(this).attr("error-id");
    var errorDescription = $(this).attr("error-description");
    var errorSolution = $(this).attr("error-solution");
    var errorImages = $(this).attr("error-images");
    var errorFiles = $(this).attr("error-files");

    $("#errorModal .modal-title").html("<p>" + errortitle + "</p>");
    $("#errorModal .modal-description").html("<p>" + errorDescription + "</p>");
    $("#errorModal .modal-solution").html("<p>" + errorSolution + "</p>");
    if (errorImages === "None" || !errorImages) {
      $("#errorModal .modal-images").html("");
    } else {
      $("#errorModal .modal-images").html(
        '<img class="no-hovering error-image-modal" src="' +
          errorImages +
          '" alt="Machine Image">'
      );
    }
    if (errorFiles === "None" || !errorFiles) {
      $("#errorModal .modal-files").html("");
    } else {
      $("#errorModal .modal-files").html("<p>" + errorFiles + "</p>");
    }
  });

  $(".image-button").click(function () {
    var images = $(this).attr("machine-images");
    $("#machineImagesModal .modal-machine-images").html(
      '<img class="no-hovering" src="' + images + '" alt="Machine Image">'
    );
  });
});
