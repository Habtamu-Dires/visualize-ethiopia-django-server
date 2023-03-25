var $ = django.jQuery;

(function($) {
    $(function() {
        var selectField = $('#id_file_type'),
            verified = $('.abcdefg'), verified2=$('.uvwxyz');

        function toggleVerified(value) {
            if(value === 'image'){
                verified.hide();
                verified2.show();
            } else if(value === 'html'){
                verified.show();
                verified2.hide();
            }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);