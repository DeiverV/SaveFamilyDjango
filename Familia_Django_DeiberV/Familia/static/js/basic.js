let  openFormFamiliar = document.querySelector("#createFamiliarBtnDiv");
let contenedorFormFamiliar = document.querySelector("#contenedorForm");
let cerrarFormFamiliar = document.querySelector("#cerrarFormFamiliar");


openFormFamiliar.addEventListener("click",(e)=>{
    contenedorFormFamiliar.style.display = 'flex';
    setTimeout(()=>{
       contenedorFormFamiliar.style.opacity = '1';
    },300)
})

cerrarFormFamiliar.addEventListener("click",(e)=>{
    contenedorFormFamiliar.style.opacity = '0';
    setTimeout(()=>{
        contenedorFormFamiliar.style.display = 'none';
    },300)
})