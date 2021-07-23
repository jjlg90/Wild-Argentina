 $(document).ready(function(){
     //Mobile navbar configuration
    $('.sidenav').sidenav({edge: "right"});
    //Slider configuration -- index.html
    $('.slider').slider({height: 600,});
    //Select dropdown -- add_experience.html
    $('select').formSelect();
    //Modal trigger
    $('.modal').modal();
    //Date picker -- register.html
    $('#birthdate').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: [1920,2015],
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    //Date picker -- add_experience.html
    $('#experience_date').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: [2015,2021],
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });

    validateMaterializeSelect();

//Validates select elements in forms -- add_experience.html
    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

//Control gallery images display - view_experience.html
function img_gallery(imgs) {
            // Get the expanded image
            var expandImg = document.getElementById("expandedImg");
            // Use the same src in the expanded image as the image being clicked on from the grid
            expandImg.src = imgs.src;
        }
  