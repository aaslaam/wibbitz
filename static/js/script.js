$(document).on("submit","form.ajax", function (event) {
    event.preventDefault();
    var $this = $(this)


      var url = $this.attr("action")
      var method = $this.attr("method")

     jQuery.ajax({
      type:method,
      url:url,
      dataType:"json",
      data: new FormData(this),
      processData:false,
      contentType:false,
      cache:false,
      success:function(data){
          var message = data["message"];
          var tittle = data["tittle"];
          var status = data["status"]
      
          Swal.fire({
              icon: status,
              title: tittle,
              text : message,
            })

            if(status == "success"){
              $this.trigger("reset");
            }

      },
      error:function(error){
          console.log("Failed 😭");
      },
     })
     
})

