window.onload = () => {

    $('#tbl-orders').DataTable({
        ajax: {
            url: '/get-order-list',
            dataSrc: function(rs) {
                return rs.data.map((el,i) => [
                     el.brand
                    ,el.model
                    ,el.type
                    ,el.date_from
                    ,el.date_to
                ]);
            }
        },
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.2/i18n/es-ES.json'
        }
    });
}