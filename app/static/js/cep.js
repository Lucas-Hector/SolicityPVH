//Usar localização atual

//Buscar no mapa

function buscaCep(){
    let cep = document.getElementById('txtCep').value;

    if (cep !== ""){
        let url = "https://brasilapi.com.br/api/cep/v1/" + cep;
        let request = new XMLHttpRequest();

        request.open("GET", url);
        request.send();

        //tratar a resposta da requisição

        request.onload = function(){
            if(request.status === 200){
                let endereco = JSON.parse(request.response);
                document.getElementById("txtRua").value = endereco.street;
                document.getElementById("txtBairro").value = endereco.neighborhood; 
            }
            else if (request.status === 404){
                alert("CEP inválido")
            }
            else{
                alert("Erro ao fazer a inserção do CEP")
            }
        }
    }
}

window.onload = function(){
    let txtCep = document.getElementById("txtCep");
    txtCep.addEventListener("blur", buscaCep);
}