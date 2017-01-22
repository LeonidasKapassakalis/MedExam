/**
 * Created by Leonidas on 14/12/2016.
 */
$(document).ready(function() {
    var oTable = $('.datatable').dataTable({
        // ...
        "processing": true,
        "serverSide": true,
        "ajax": "{% url 'order_list_json' %}"
    });
    // ...
});
