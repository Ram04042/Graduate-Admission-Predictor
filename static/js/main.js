$(function() {

         $("#gre_error").hide();
         $("#toefl_error").hide();
         $("#uni_error").hide();
         $("#sop_error").hide();
         $("#lor_error").hide();
		 

         var gre_error = false;
         var toefl_error = false;
         var uni_error = false;
         var sop_error = false;
         var lor_error = false;
		 var cgpa_error = false;

         $("#gre_score").focusout(function(){
            check_gre();
         });
		 
		 $("#toefl_score").focusout(function(){
            check_toefl();
         });
		 
		 $("#uni_rating").focusout(function(){
            check_uni();
         });
		 
		 $("#sop").focusout(function(){
            check_sop();
         });
		 
		 $("#lor").focusout(function(){
            check_lor();
         });
		 
		 $("#cgpa").focusout(function(){
            check_cgpa();
         });
		 
		 
		 
		 
         

         function check_gre() {
            var gre = $("#gre_score").val();
            if (gre <= 340) {
               $("#gre_error").hide();
               $("#gre_score").css("border-bottom","2px solid #34F458");
            } else {
               $("#gre_error").html("GRE Score cannot be greater than 340");
               $("#gre_error").show();
               $("#gre_score").css("border-bottom","2px solid #F90A0A");
               gre_error = true;
			   console.log("error");
            }
         }
		 
		 function check_toefl() {
            var toefl = $("#toefl_score").val();
            if (toefl <= 120) {
               $("#toefl_error").hide();
               $("#toefl_score").css("border-bottom","2px solid #34F458");
            } else {
               $("#toefl_error").html("TOEFL Score cannot be greater than 120");
               $("#toefl_error").show();
               $("#toefl_score").css("border-bottom","2px solid #F90A0A");
               toefl_error = true;
			   console.log("error");
            }
         }
		 
		 function check_uni() {
            var uni = $("#uni_rating").val();
            if (uni <= 5) {
               $("#uni_error").hide();
               $("#uni_rating").css("border-bottom","2px solid #34F458");
            } else {
               $("#uni_error").html("Give University Rating out of 5");
               $("#uni_error").show();
               $("#uni_rating").css("border-bottom","2px solid #F90A0A");
               uni_error = true;
			   console.log("error");
            }
         }
		 
		 function check_sop() {
            var sop = $("#sop").val();
            if (sop <= 5) {
               $("#sop_error").hide();
               $("#sop").css("border-bottom","2px solid #34F458");
            } else {
               $("#sop_error").html("Give SOP Rating out of 5");
               $("#sop_error").show();
               $("#sop").css("border-bottom","2px solid #F90A0A");
               sop_error = true;
			   console.log("error");
            }
         }
		 
		 function check_lor() {
            var lor = $("#lor").val();
            if (lor <= 5) {
               $("#lor_error").hide();
               $("#lor").css("border-bottom","2px solid #34F458");
            } else {
               $("#lor_error").html("Give SOP Rating out of 5");
               $("#lor_error").show();
               $("#lor").css("border-bottom","2px solid #F90A0A");
               lor_error = true;
			   console.log("error");
            }
         }
		 
		 function check_cgpa() {
            var cgpa = $("#cgpa").val();
            if (cgpa <= 10) {
               $("#cgpa_error").hide();
               $("#cgpa").css("border-bottom","2px solid #34F458");
            } else {
               $("#cgpa_error").html("CGPA cannot be greater than 10");
               $("#cgpa_error").show();
               $("#cgpa").css("border-bottom","2px solid #F90A0A");
               cgpa_error = true;
			   console.log("error");
            }
         }
		 
		 
            
});
