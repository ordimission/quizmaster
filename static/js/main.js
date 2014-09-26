
function onClickQuestionnaireHandler(event) {
   $.ajax({
            type: "GET",
	    dataType: 'json',
            url: "api/questionnaires/"+event.data.questionnaireId+"?shuffle=1&size=10",
            /*data: { id : "questionnaire_id" },*/
            success: function( questionnaire ){
		$("#question_table > tbody").empty()
                for(var i = 0; i< questionnaire.questions.length; i++){
                    var tableRow = "<tr><td>" + questionnaire.questions[i].number + "</td><td>";
		    tableRow +="<table><thead>"+ questionnaire.questions[i].label+"</thead><tbody>";
		    for (var j=0; j<questionnaire.questions[i].choices.length; j++) {	
		       tableRow +="<tr><td><input type='checkbox' id='checkbox_choice"+i+"_"+j+"'/>"+questionnaire.questions[i].choices[j].label +"</td></tr>";	
		    } 
		    tableRow += "</tbody></table></td></tr>";
                    $("#question_table > tbody:last").append(tableRow);
                }
            }
    });
} 


$(document).ready(function(){
    $.ajax({
            type: "GET",
	    dataType: 'json',
            url: "api/questionnaires/",
            /*data: { id : "questionnaire_id" },*/
            success: function( questionnaires ){
                for(var i = 0; i< questionnaires.length; i++){
                    var tableRow = "<tr><td><button id='button_questionnaire_"+questionnaires[i]._id+"'>" + questionnaires[i]._id + "</button></td><td>" + questionnaires[i].name + "</td></tr>";
                    $("#questionnaire_table > tbody:last").append(tableRow);
                    $("#button_questionnaire_"+questionnaires[i]._id).click({questionnaireId:questionnaires[i]._id}, onClickQuestionnaireHandler);		
                }
            }
    });
});
