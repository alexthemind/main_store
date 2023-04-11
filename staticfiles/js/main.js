window.onload = () => {
    let brand = document.querySelector('select[name="brand"]');
    let model = document.querySelector('select[name="model"]');
    let type = document.querySelector('select[name="type"]');
    let from = document.querySelector('input[name="from"]');
    let to = document.querySelector('input[name="to"]');
    let btnSend = document.getElementById('btn-send');
    let success = document.getElementById('success');
    let error = document.getElementById('error');
    let error_date1 = document.getElementById('error_date1');
    let label_loading = document.getElementById('label-loading');
    let token = document.querySelector('input[name="csrfmiddlewaretoken"]');


    let getBrands = function() {
        fetch('./get-brands').then(rs => rs.json()).then(rs => {
            setIntobrands(brand,rs.data);
        });
    }

    let getModels = function(brand) {
        fetch('./get-models/' + brand).then(rs => rs.json()).then(rs => {
            model.innerHTML = '<option value="0">Elija un modelo</option>';
            setIntobrands(model,rs.data);
        });
    }

    let getTypes = function(model) {
        fetch('./get-types/' + model).then(rs => rs.json()).then(rs => {
            type.innerHTML = '<option value="0">Elija un modelo</option>';
            setIntobrands(type,rs.data);
        });
    }

    

    let setIntobrands = function(parent,items) {
        items.map(el => {
            let option = document.createElement('option');
                option.value = el.id;
                option.innerText = el.name || el.type;

            parent.appendChild(option);
        });
    }


    let setNoticeSuccess = function() {
        let icon = label_loading.querySelector('i');
        let span = label_loading.querySelector('span');

        icon.className = 'fa fa-check text-6xl text-green-500';
        span.innerHTML = '';
    }

    /**
     * EVENTOS DE CAMBIO EN ELEMENTOS
     * DEL CLIENTE
     */
    brand.onchange = () => {
        getModels(brand.value);
    }
    model.onchange = () => {
        getTypes(model.value);
    }
    btnSend.onclick = () => {
        validate = true;
        formData = new FormData();

        if(brand.value == 0)
        {
            validate = false;
        }
        else if(model.value == 0)
        {
            validate = false;
        }
        else if(type.value == 0)
        {
            validate = false;
        }
        else if(from.value.length == 0)
        {
            validate = false;
        }
        else if(to.value.length == 0)
        {
            validate = false;
        }

        if(from.value > to.value)
        {
            error_date1.classList.add('active');
            error.classList.remove('active');
            
            return  false;
        }

        /** ANEXO LAS VARIABLES */
        formData.append('brand',brand.value);
        formData.append('model',model.value);
        formData.append('type',type.value);
        formData.append('from',from.value);
        formData.append('to',to.value);

        if(validate != false)
        {
            label_loading.classList.add('active');

            fetch('./set-order/',{
                method: 'POST',
                headers: {
                    'X-CSRFToken': token.value
                },
                body: formData
            }).then(rs => rs.json()).then(rs => {
                if(rs.action != false)
                {
                    setNoticeSuccess();
                    success.classList.add('active');
                    error.classList.remove('active');
                    error_date1.classList.remove('active');

                    setTimeout(() => {
                        brand.value = 0;
                        model.value = 0;
                        type.value = 0;
                        from.value = '';
                        to.value = '';
                        success.classList.remove('active');
                        label_loading.classList.remove('active');
                    },2000);
                }
            })

        }
        else
        {
            label_loading.classList.remove('active');
            error_date1.classList.remove('active');
            success.classList.remove('active');
            error.classList.add('active');
        }
    };

    /**
     * INICIO DE LOS PROCESOS DE CARGA
     */
    getBrands();

}
