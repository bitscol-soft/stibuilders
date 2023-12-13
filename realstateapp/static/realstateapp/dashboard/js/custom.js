
// Image Preview 

$("#upload-image").change(function () {
  var reader = new FileReader();
  reader.readAsDataURL(this.files[0]);
  reader.onload = function (event) {
    var ImgSource = event.target.result;
    $("#image-preview").attr("src", ImgSource);
  };
});
// Agent Logo Logo Preview 
$("#upload-logo").change(function () {
  var reader = new FileReader();
  reader.readAsDataURL(this.files[0]);
  reader.onload = function (event) {
    var logoSource = event.target.result;
    $("#logo-preview").attr("src", logoSource);
  };
  
});

// Profile Image Preview 
$("#upload-profile").change(function () {
  var reader = new FileReader();
  reader.readAsDataURL(this.files[0]);
  reader.onload = function (event) {
    var logoSource = event.target.result;
    $("#profile-preview").attr("src", logoSource);
  };
  
});

// Checking Payment Installment 
$('#installment').on('change',function(){
  if($('#installment').is(":checked")){
    $('#payment-installment').show()
  }else {
    $('#payment-installment').hide()
  }
})
$('#payment-installment').on('change',function(){

})
$('#selected').click(function(){
  let propertyType=$('#property-type').val()

  if(propertyType=='appartment'){

    $('#appartment').show()
    $('#plot').hide()
  }
  if(propertyType=='plot'){
    $('#plot').show()
    $('#appartment').hide()
  }
});

// Checking Agent Type 
$('#select-agent').click(function(){
  let propertyType=$('#agent-type').val()

  if(propertyType=='person'){
    document.querySelector('#person')
    $('#person').show()
    $('#company').hide()
  }
  if(propertyType=='company'){
    $('#company').show()
    $('#person').hide()
  }
})

// Payment Installation

// Dynamic Owner Form 
function addOwner(){
  let rowId=Math.floor(Math.random() * 100)

  let row =`<div class="row" id="row-${rowId}">
              <div class="col-md-4 col-12">
                  <div
                      class="form-group">
                      <label
                          for="owner-name"
                          class="form-label">Owner Name</label>
                      <input
                          type="text"
                          class="form-control"
                          name="owner_name"
                          id="owner-name">
                  </div>
              </div>
              <div class="col-md-4 col-12">
                  <div
                      class="form-group">
                      <label
                          for="owner-name"
                          class="form-label">Ownership(%)</label>
                      <input
                          type="number"
                          class="form-control"
                          name="owner_name"
                          id="owner-name">
                  </div>
              </div>
              <div class="col-md-4 col-12 mt-4">
                  <button type="button" class="btn btn-primary btn-sm" onclick="addOwner()"><i class="fa fa-plus"></i>Add Owner</button>
                  <button type="button" class="btn btn-danger btn-sm" onclick="removeOwner(${rowId})"><i class="fa fa-trash-o" ></i>Add Owner</button>
              </div>
          </div>`;
      $('#owner-info').append(row);
}

// Dynamic Owner Remove 
function removeOwner(rowId) {
  let data=`row-${rowId}`
  $(`#${data}`).remove()
}
// Dynamic Document Form 
function addDocument(){
  let documentRowID=Math.floor(Math.random() * 100)

  let documentRow =`<div class="row" id="doc-row-${documentRowID}">
                      <div class="col-md-4 col-12">
                      <div
                          class="form-group">
                          <label
                              for="document-name"
                              class="form-label">Document Name</label>
                          <input
                              type="text"
                              class="form-control"
                              name="document_name"
                              id="document-name">
                      </div>
                    </div>
                    <div class="col-md-4 col-12">
                      <div
                          class="form-group">
                          <label
                              for="document-ile"
                              class="form-label">Choose Document</label>
                          <input
                              class="form-control"
                              type="file"
                              id="document-file"
                              multiple=""
                              name="document_file">
                      </div>
                    </div>
              <div class="col-md-4 col-12 mt-4">
                  <button type="button" class="btn btn-primary btn-sm" onclick="addDocument()"><i class="fa fa-plus"></i>Add Owner</button>
                  <button type="button" class="btn btn-danger btn-sm" onclick="removeDocument(${documentRowID})"><i class="fa fa-trash-o" ></i>Add Owner</button>
              </div>
          </div>`;
      $('#legal-document').append(documentRow);
}

// Dynamic Remove Form 
function removeDocument(rowId) {
  let dataRow=`doc-row-${rowId}`
  $(`#${dataRow}`).remove()
}

// Delete Alert 
$(document).on('click','.delete-btn',function(e){

  e.preventDefault();

  let form=$(this).closest('form');
  Swal.fire({
      title:"Are your sure want to delete this page !",
      text:'Once deleted, you will not be able to recover',
      icon:'warning',
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: 'Delete',
      denyButtonText: `Don't Delete`,
  }).then((willDelete)=>{
      if (willDelete.isConfirmed) {
          form.submit();
      }else{
          Swal.fire('Your Data is safe','', 'info')
      }
  });
});


// Multile Slider  Images preview
function previewSliderImages() {
  var preview = $("#preview-slider-images").empty();
  if (this.files) $.each(this.files, readAndPreview);

  function readAndPreview(i, file) {
    if (!/\.(jpe?g|png|gif|webp|svg)$/i.test(file.name)) {
      return alert(file.name + " is not an image");
    } // else...

    var reader = new FileReader();
    $(reader).on("load", function () {
      preview.append($("<img />", { src: this.result, height: 100 }));
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
