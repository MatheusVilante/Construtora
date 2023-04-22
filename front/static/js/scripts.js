
var global_dados_api_get = ''
var global_id_insert = ''
function corrigir_titulo(mySentence){
    mySentence = mySentence.replaceAll("_", " ");
    words = mySentence.split(" ");
    response = []
    for (x=0; x < words.length;x++){
        word = words[x];
        response.push(word[0].toUpperCase() + word.substring(1))
    }
    return response.join(' ');
}
function todos(){
var checked =  $(".ckb-all").prop('checked');
$(".ckbsel").prop('checked',checked)
}
function objectifyForm(formArray) {
    var returnArray = {};
    for (var i = 0; i < formArray.length; i++){
    var element = formArray[i];
    if (element.type === 'checkbox') {
        returnArray[element.name] = element.checked;
    } else {
        returnArray[element.name] = element.value;
    }
    }
    return returnArray;
}

function zerar_form(){
        $('#cadastro').each (function(){
        this.reset();
        });
    }

function adicionar(tabela,campos){
    var data = objectifyForm($('#cadastro').serializeArray());
    var valida = true;
    var csrf_token = $("input[name='csrfmiddlewaretoken']").val(); // obter token CSRF
    data += "&csrfmiddlewaretoken=" + csrf_token;
    
    campos_msg = 'Favor Preencher ';
    for (i=0; i<campos.length;i++){
    if (data[campos[i]] == null || data[campos[i]] == ''){
        if (valida == false){
            campos_msg+=', ';
        }
        campos_msg+=corrigir_titulo(campos[i]);
        valida=false;
    }
    }
    if (valida == false){
        alert(campos_msg)
    }else{
        // alert(data)
    var url = '/api/v1/'+tabela+'/';
    var method = 'POST';
    if (data.id != ''){
        url += data.id+'/'
        method = 'PUT';
    }
    $.ajax({url:url,type:method,data:data, error: function(e) {
        var campos = '';
        $.each(e.responseJSON,function(index,value){
            campos += index+': '+value+'\n\n'
        });
        alert(campos)
        },
        success: function (data){
            carregar();          
            alert ('Sucesso!');
        },dataType:'json'});
    }

}

var datatable = null


function capitalizeFirstLetter(string) {
    string = string.split('_').join(' ');
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function criar_select(id, url,titulo,filtro={}) {
    var s = '';

    $.ajax({
        url: url,
        type: 'POST',
        data:filtro,
        error: function(e) {
        // alert(e)
        },
        
        success: function (data){
            s = '<option value=""> selecionar '+capitalizeFirstLetter(titulo)+'</option>';
            $.each(data, function(key, value) {
                s += '<option value="' + value[0] + '">' + value[1] + '</option>';
            });
            s += '</select>' ;
            $("#"+id).html(s);
        },dataType:'json'});
}

function listar(tabela,campos,id,tabela_tipo = 'datatablesSimple', indexphoto = null){
    // alert(tabela_tipo)
    if ((tabela_tipo == 'datatablesSimple')&&(datatable != null)){
        datatable.destroy()     

    }
    var url = '/api/v1/'+tabela+'/'
    if (id !=null){
        url = '/api/v1/'+tabela+'/?id='+id
}

    $.get(url, function(data){
        global_dados_api_get = data;
        var html = '<thead><tr><th class="todos"><input type="checkbox" class="ckb-all" onclick="todos();" value="" /> Todos</th>';

        for (i=0; i<campos.length;i++){

            html+= '<th>'+corrigir_titulo(campos[i])+'</th>';
        }
        html += '</tr></thead>';
        html += '<tbody>'  
        $.each(data, function(index,value){
            html += '<tr>';
            var id = value['id']
            html+= '<td><input type="checkbox" class="ckbsel" name="ckb-'+id+'"  value="'+id+'" /></td>';
            for (i=0; i<campos.length;i++){
                if(i == indexphoto){
                    html+= `<td><img src="${value[campos[i]]}"></img></td>`;
                }else{
                    html+= '<td>'+value[campos[i]]+'</td>';
                }
            }
            html += '</tr>';
        });

        
        html += '</tbody>';

        $("#"+tabela_tipo).html(html);

        datatable = $("#"+tabela_tipo).DataTable()
    },'json');
}


function editar(){
    var selecionados = []
    $('.ckbsel:checked').each(function () {
        selecionados.push(this.value)
    });
    if (selecionados.length > 1){
        alert('Favor selecionar apenas uma linha')
    }else if (selecionados.length == 0){
        alert('Favor selecionar uma linha')
    }else{
        $("#openModa\l").click();
        var id_selecionado = selecionados[0];
        console.log(global_dados_api_get)
        $.each(global_dados_api_get, function(index,value){
            if (value.id == id_selecionado){
                $.each(value, function(index2,value2){
                    $('#'+index2).val(value2);
                });
            }            
        });
    }
}

function excluir(tabela){
    var selecionados = []
    $('.ckbsel:checked').each(function () {
        selecionados.push(this.value)
    });
    if (selecionados.length == 0){
        alert('Favor selecionar uma linha')
    }else{
        // var id_selecionado = selecionados[0];
        for (var i = 0; i < selecionados.length; i++) {
            var url = '/api/v1/'+tabela+'/';
            var method = 'DELETE';
            url += selecionados[i]+'/'
            $.ajax({url:url,type:method, error: function(e) {
            var campos = '';
            $.each(e.responseJSON,function(index,value){
                campos += index+': '+value+'\n\n'
            });     
                alert(campos)
                },
            success: function (data){
                // alert(selecionados)
            },dataType:'json'})
        };
        carregar();
        alert ('Excluido com Sucesso!');
    }
}


// var global_token = window.localStorage.getItem('global_token');
// function login(){
//     // alert('11')
//     var username = $("#username").val();
//     var password = $("#password").val();
//     if (username == ''){
//         alert('Username is required');
//     }else{
//         data = {"username":username,"password":password,"redirecionar":true};
//         $.ajax({url:'/api/v1/login/',
//                 type:'POST',
//                 data:data, 
//                 error: function(e) {
//                     alert(e);
//                 },
//                 success: function (data){
//                     if (data.token != null){
//                         window.localStorage.setItem('global_token', data.token); 
//                         // alert(data.token)
//                         guardar_token();
//                         $("form").submit()
//                         // window.location.href = "/teste2" 
//                     }else{
//                         // alert(data)
//                     }
//                 },dataType:'json'});
//     }
// }


// function guardar_token(){

//     $.ajax({
//         url: '/api/v1/login/',
//         type: 'GET',
//         // Fetch the stored token from localStorage and set in the header
//         headers: {"Authorization": "Token "+global_token}
//         ,error: function(e) {
//         // alert(e);
//         },
//         success: function (data){
//             // alert("sucesso")
//         },dataType:'json'});

// }
