$(document).ready(function () {
    //Floor Size And Units
    $("#floor-number").on("keyup", function () {
      var numberOfFloor = parseInt($("#floor-number").val());
  
      var units = "";
      var floors = "";
      var resizeBtns = "";
      for (i = numberOfFloor - 1; i > 0; i--) {
        units += `<div class="d-flex align-items-center">
            <div class="d-flex align-items-center my-0 mx-1 py-0"><span class="floor-mr-10">Floor-Size-${i}: </span><div class="unit-border"><input type="text" class="form-control border-0" id="floor-size-no-${i}" />
            </div>
            </div>
            <div class="d-flex align-items-center my-0 mx-1 py-0">
            <span class="floor-mr-10">Total Unit: </span><div class="unit-border"><input type="text" class="form-control border-0" min="1" id="unit-num-${i}" onkeyup="floorInfo(${i})" />
            </div>
            </div>
            </div>`;
  
        floors += `<div id="floor-no-${i}" class="m-0 p-0"><div class="floor-border w-full"><input class="form-control border-0" /></div></div>`;
        resizeBtns += `<button type="button" class="btn btn-primary btn-sm mb-1" data-bs-toggle="modal" data-bs-target="#modal-center" onclick="calculateSize(${i})" id="resize-btn-${i}">Resize</button>`;
      }
      floors += `<div class="floor-border p-2 text-center bg-danger text-white">Ground Floor</div>`;
      $("#unit-items").html(units);
      $("#floor-items").html(floors);
      $("#resize-btns").html(resizeBtns);
    });
  
    $(".accept-value").on("keyup", function () {
      let items = parseInt($(".accept-value").val());
      var rows = "";
      for (i = 1; i <= items; i++) {
        rows += `<div class="floor-item d-flex" id="row-${i}" onclick="modalOpen(this)"><div class="p-2 border-1 w-full single-unit">${i}</div></div>`;
      }
      $("#table").html(rows);
  
      $(".single-unit .unit-size-input").click(function (e) {
        e.preventDefault();
        $("#popup-modal").addClass("d-none");
      });
      $(".single-unit").removeEventListener("click");
    });
  
    $("td.floor-item").on("click", function () {
      console.log("clicked");
      $(".popup-modal").removeClass("d-none");
    });
  
    $("#upload-image").change(function () {
      var reader = new FileReader();
      reader.readAsDataURL(this.files[0]);
      reader.onload = function (event) {
        var ImgSource = event.target.result;
        $("#image-preview").attr("src", ImgSource);
      };
    });
  
    // Multile Slider Images preview
    function previewSliderImages() {
      var preview = $("#preview-slider-images").empty();
      if (this.files) $.each(this.files, readAndPreview);
  
      function readAndPreview(i, file) {
        if (!/\.(jpe?g|png|gif|webp|svg)$/i.test(file.name)) {
          return alert(file.name + " is not an image");
        } // else...
  
        var reader = new FileReader();
        $(reader).on("load", function () {
          preview.append($("<img/>", { src: this.result, height: 100 }));
        });
        reader.readAsDataURL(file);
      }
    }
    $("#upload-slider-images").on("change", previewSliderImages);
  
    // Multile Gallery  Images preview
    function previewGalleryImages() {
      var preview = $("#preview-gallery-images").empty();
      if (this.files) $.each(this.files, readAndPreview);
  
      function readAndPreview(i, file) {
        if (!/\.(jpe?g|png|gif|webp|svg)$/i.test(file.name)) {
          return alert(file.name + " is not an image");
        } // else...
  
        var reader = new FileReader();
        $(reader).on("load", function () {
          preview.append($("<img/>", { src: this.result, height: 100 }));
        });
        reader.readAsDataURL(file);
      }
    }
    $("#gallery-images").on("change", previewGalleryImages);
  
    // Multile Floor Plan Images preview
    function previewFloorImages() {
      var preview = $("#preview-floor-plan-images").empty();
      if (this.files) $.each(this.files, readAndPreview);
  
      function readAndPreview(i, file) {
        if (!/\.(jpe?g|png|gif|webp|svg)$/i.test(file.name)) {
          return alert(file.name + " is not an image");
        } // else...
  
        var reader = new FileReader();
        $(reader).on("load", function () {
          preview.append($("<img/>", { src: this.result, height: 100 }));
        });
        reader.readAsDataURL(file);
      }
    }
    $("#floor-plan-images").on("change", previewFloorImages);
  
    var tooltipTriggerList = [].slice.call(
      document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
    });
  });
  
  function floorInfo(item) {
    let floorSizeId = `floor-size-no-${item}`;
    let unitNumberId = `unit-num-${item}`;
    let floorNumberId = `floor-no-${item}`;
  
    let floorSize = parseInt($(`#${floorSizeId}`).val());
    let unitNumber = parseInt($(`#${unitNumberId}`).val());
    var singleFloor = "";
    let singleFloorSize = floorSize / unitNumber;
    let width = 100 / unitNumber;
    for (j = 1; j <= unitNumber; j++) {
      singleFloor += `<div class="floor-border" style="width: ${width}% !important"><input class="form-control border-0" value="${singleFloorSize}" onkeyup="singleFlatSize(${item})" /></div>`;
    }
    $(`#${floorNumberId}`).addClass("d-flex flex-wrap");
    $(`#${floorNumberId}`).html(singleFloor);
  }
  
  function calculateSize(floorId) {
    let flatParentId = $(`#floor-no-${floorId}`);
    let defaultFlatSize = flatParentId.children().children().val();
    let totalFlat = flatParentId.children().length;
    var floorSizeInput = "";
    let modalBody = $("#input-modal-body");
    $("#calculated-size").attr("floor-item-no", `floor-no-${floorId}`);
    for (k = 1; k <= totalFlat; k++) {
      floorSizeInput += `<input type="text" class="form-control my-2" value="${defaultFlatSize}" onkeyup="changeFlatSize(${k})" id="modal-input-${k}" floor-no="floor-size-no-${floorId}" total-flat="${totalFlat}" />`;
    }
    modalBody.html(floorSizeInput);
  }
  function changeFlatSize(inputItems,event) {
    let inputId = $(`#modal-input-${inputItems}`);
    let targetFloor = inputId.attr("floor-no");
    let Flats = inputId.attr("total-flat");
    let targetFloorSizeValue = parseInt($(`#${targetFloor}`).val());
    if (inputItems == 1) {
  
      let dueSize = targetFloorSizeValue - parseInt(inputId.val());
      let leftInputs = parseInt(Flats) - 1;
      let dueSingleSize = dueSize / leftInputs;
      inputId.nextAll().val(dueSingleSize);
    }
    if (inputItems == 2) {
      let usedOne = parseInt($("#modal-input-1").val()) + parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedOne);
      let leftInputs = parseInt(Flats) - 2;
      let dueSingleSize = dueSize / leftInputs;
      $(`#modal-input-2`).nextAll().val(dueSingleSize);
    }
    if (inputItems == 3) {
      let usedTwo =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedTwo);
      let leftInputs = parseInt(Flats) - 3;
      let DueSingleSize = dueSize / leftInputs;
      $(`#modal-input-3`).nextAll().val(DueSingleSize);
    }
    if (inputItems == 4) {
      let usedThree =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt($("#modal-input-3").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedThree);
      let leftInputs = parseInt(Flats) - 4;
      let DueSingleSize = dueSize / leftInputs;
  
      $(`#modal-input-4`).nextAll().val(DueSingleSize);
    }
    if (inputItems == 5) {
      let usedFour =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt($("#modal-input-3").val()) +
        parseInt($("#modal-input-4").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedFour);
      let leftInputs = parseInt(Flats) - 5;
      let DueSingleSize = dueSize / leftInputs;
  
      $(`#modal-input-5`).nextAll().val(DueSingleSize);
    }
    if (inputItems == 6) {
      let usedFive =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt($("#modal-input-3").val()) +
        parseInt($("#modal-input-4").val()) +
        parseInt($("#modal-input-5").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedFive);
      let leftInputs = parseInt(Flats) - 6;
      let DueSingleSize = dueSize / leftInputs;
  
      $(`#modal-input-6`).nextAll().val(DueSingleSize);
    }
    if (inputItems == 7) {
      let usedSix =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt($("#modal-input-3").val()) +
        parseInt($("#modal-input-4").val()) +
        parseInt($("#modal-input-5").val()) +
        parseInt($("#modal-input-6").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedSix);
      let leftInputs = parseInt(Flats) - 7;
      let DueSingleSize = dueSize / leftInputs;
  
      $(`#modal-input-7`).nextAll().val(DueSingleSize);
    }
    if (inputItems == 8) {
      let usedSeven =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt($("#modal-input-3").val()) +
        parseInt($("#modal-input-4").val()) +
        parseInt($("#modal-input-5").val()) +
        parseInt($("#modal-input-6").val()) +
        parseInt($("#modal-input-7").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedSeven);
      let leftInputs = parseInt(Flats) - 8;
      let DueSingleSize = dueSize / leftInputs;
  
      $(`#modal-input-8`).nextAll().val(DueSingleSize);
    }
    if (inputItems == 9) {
      let usedEight =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt($("#modal-input-3").val()) +
        parseInt($("#modal-input-4").val()) +
        parseInt($("#modal-input-5").val()) +
        parseInt($("#modal-input-6").val()) +
        parseInt($("#modal-input-7").val()) +
        parseInt($("#modal-input-8").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usedEight);
      let leftInputs = parseInt(Flats) - 9;
      let DueSingleSize = dueSize / leftInputs;
  
      $(`#modal-input-9`).nextAll().val(DueSingleSize);
    }
    if (inputItems == 10) {
      let usednine =
        parseInt($("#modal-input-1").val()) +
        parseInt($("#modal-input-2").val()) +
        parseInt($("#modal-input-3").val()) +
        parseInt($("#modal-input-4").val()) +
        parseInt($("#modal-input-5").val()) +
        parseInt($("#modal-input-6").val()) +
        parseInt($("#modal-input-7").val()) +
        parseInt($("#modal-input-8").val()) +
        parseInt($("#modal-input-9").val()) +
        parseInt(inputId.val());
      let dueSize = targetFloorSizeValue - parseInt(usednine);
      let leftInputs = parseInt(Flats) - 10;
      let DueSingleSize = dueSize / leftInputs;
  
      $(`#modal-input-10`).nextAll().val(DueSingleSize);
    }
  }
  
  function saveValueToFloor() {
    
    let inertInto = $("#calculated-size").attr("floor-item-no");
    let html=document.getElementById('input-modal-body').innerHTML
  // document.getElementById(inertInto).innerHTML=html
  //   //inertInto.html(html);
  //   alert(inertInto)
    let value1 = document.getElementById("modal-input-1").value;
    let value2 = document.getElementById("modal-input-2").value;
    let value3 = document.getElementById("modal-input-3").value;
    let value4 = document.getElementById("modal-input-4").value;
    let value5 = document.getElementById("modal-input-5").value;
    let value6 = document.getElementById("modal-input-6").value;
    let value7 = document.getElementById("modal-input-7").value;
    let value8 = document.getElementById("modal-input-8").value;
    let value9 = document.getElementById("modal-input-9").value;
    let value10 = document.getElementById("modal-input-10").value;
    $(`#${inertInto} input:nth-child(1)`).val(value1);
    $(`#${inertInto} input:nth-child(2)`).val(value2);
    $(`#${inertInto} input:nth-child(3)`).val(value3);
    $(`#${inertInto} input:nth-child(4)`).val(value4);
    $(`#${inertInto} input:nth-child(5)`).val(value5);
    $(`#${inertInto} input:nth-child(6)`).val(value6);
    $(`#${inertInto} input:nth-child(7)`).val(value7);
    $(`#${inertInto} input:nth-child(8)`).val(value8);
    $(`#${inertInto} input:nth-child(9)`).val(value9);
    $(`#${inertInto} input:nth-child(10)`).val(value10);
   
  
  }
  
  function modalOpen(row) {
    var selectedRow = $(row).attr("id");
    $("#popup-modal").removeClass("d-none");
    $("#target-row").val(selectedRow);
    $(".single-unit").removeEventListener("click");
  }
  $("#modal-close").on("click", function () {
    $("#popup-modal").addClass("d-none");
  });
  $("#modal-submit").on("click", function () {
    $("#popup-modal").addClass("d-none");
    var flats = "";
    var totalUnits = parseInt($("#units").val());
    var insertInto = $("#target-row").val();
  
    for (i = 1; i <= totalUnits; i++) {
      flats += `<div class="p-2 single-unit"><input class="form-control w-full border-0 unit-size-input"></div>`;
    }
    $(`#${insertInto}`).html(flats);
  
    // alert($('#is-duplex'));
    if ($("#is-duplex")[0].checked) {
      var duplexWith = $("#duplex-sibling").val();
      if (duplexWith == "up-floor") {
        $(`#${insertInto}`).addClass("duplex-with-top");
        $(".duplex-with-top").prev().addClass("duplex-top");
      }
      if (duplexWith == "down-floor") {
        $(`#${insertInto}`).addClass("duplex-with-bottom");
        $(".duplex-with-bottom").next().addClass("duplex-bottom");
      }
    }
  });
  $("#is-duplex").click(function () {
    $("#duplex").toggleClass("d-none");
  });
  $(".single-unit").removeEventListener("click");
  
  $(".single-unit").removeEventListener("click");
  