$(document).ready(function(){
    $('select.org_dropdown').select2();
    $('select.group_dropdown').select2();
    $('#groups_dropdown_box_1').show();
    $('#ownership-form').submit(function(e){
        $('#org_group_error').hide();
        $('.org_dropdown').css('border', '');
        let org = $('#org_dropdown').find(':selected').val();
        if(org == '0'){
            e.preventDefault();
            $('#org_group_error').show();
            $('.org_dropdown').css('border', '2px solid red');
        }      
    });

    /**
     * Add another group
     */
    $('#add_another_group').click(function(){
        let all_visible = false;
        for(let i=1; i <= $('.group_dropdown_box').length; i++){
          if ($('#groups_dropdown_box_' + i).is(':hidden')){
            $('#groups_dropdown_box_' + i).fadeIn();
            all_visible = true;
            break;
          }
        }
        if(!all_visible){
          $(this).hide();
        }
      });
});