$(function() {
    $('#default').stepy({
        backLabel: 'Previous',
        block: true,
        nextLabel: 'Next',
        titleClick: true,
        titleTarget: '.stepy-tab'
    });
});

$(document).ready(function () {
    var form = $("#wizard-validation-form");
    form.validate({
        errorPlacement: function errorPlacement(error, element) {
            element.after(error);
        }
    });
    form.children("div").steps({
        headerTag: "h3",
        bodyTag: "section",
        transitionEffect: "slideLeft",
        onStepChanging: function (event, currentIndex, newIndex) {
            form.validate().settings.ignore = ":disabled,:hidden";
            return form.valid();
        },
        onFinishing: function (event, currentIndex) {
            form.validate().settings.ignore = ":disabled";
            return form.valid();
        },
        onFinished: function (event, currentIndex) {
            alert("Submitted!");
        }
    }).validate({
        errorPlacement: function errorPlacement(error, element) {
            element.after(error);
        },
        rules: {
            confirm: {
                equalTo: "#password"
            }
        }
    });
});
