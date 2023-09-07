// !NAVBAR-START
//* navbar kategori gizleme 
let navbarEye = document.getElementById('navbar-eye')
let navbarKategori = document.getElementById('navbar-kategori')
let navbarXmark = document.getElementById('navbar-xmark') 

if(navbarEye){
    navbarEye.addEventListener('click', toggleNavbar)
}
if(navbarXmark){
    navbarXmark.addEventListener('click',toggleNavbar)
}

function toggleNavbar(){
    navbarEye.classList.toggle('navbar-eye')
    navbarXmark.classList.toggle('navbar-xmark')
    navbarKategori.classList.toggle('navbar-kategori')
}

// !LİNK GRUBU DETAY BÖLÜMÜ
// Link grubu data ile yaptım
let aktifDiv = null;
function linkMenu(link){
    const linkGrupId = link.dataset.target;
    const linkGrup = document.getElementById(linkGrupId);
    if (aktifDiv !== null && aktifDiv !== linkGrup) {
        aktifDiv.style.display = "none";
    }
    linkGrup.style.display = linkGrup.style.display === "block" ? "none" : "block";
    aktifDiv = linkGrup.style.display === "block" ? linkGrup : null;
}

//!NAVBAR-HAMBURGER-MENU-START
function barMenu(){
    const barOpenElements = document.querySelectorAll('.bar-menu')
    barOpenElements.forEach((element) => {
        element.addEventListener('click',() =>{
            const hamburgerMenu = document.querySelector('.hamburger-menu')
            hamburgerMenu.classList.add('hamburger-menu-aktif')
            if(hamburgerMenu.classList.contains('hamburger-menu-aktif')){
            }
                
        })
    })

    const ok = document.querySelectorAll('.ok')
    ok.forEach((e) => {
        e.addEventListener('click', ()=>{
            const hamburgerMenu = document.querySelector('.hamburger-menu')
            if(hamburgerMenu.classList.contains('hamburger-menu-aktif')){
            hamburgerMenu.classList.remove('hamburger-menu-aktif')
            }
        })
    })
    
}
barMenu()


//* üst-div-TR
//* üst div'de bulunan TR bölümünün hamburger-menu yapısı
const trAc = document.querySelectorAll('#tr')
trAc.forEach((element) =>{
    element.addEventListener('click', () =>{
        const hamburgerMenuTr = document.querySelector('.hamburger-menu-tr')
        hamburgerMenuTr.classList.toggle('hamburger-menu-aktif')
    });

    const ok = document.querySelectorAll('#ok-tr')
    ok.forEach((e) => {
        e.addEventListener('click', ()=>{
            const hamburgerMenuTr = document.querySelector('.hamburger-menu-tr')
            if(hamburgerMenuTr.classList.contains('hamburger-menu-aktif')){
            hamburgerMenuTr.classList.remove('hamburger-menu-aktif')
            }
        })
    })
});

//*üst-div-Tüm-Türkiye 
//* üst div'de bulunan Tüm Türkiye bölümünün hamburger-menu-yapısı
const tumTrAc = document.querySelectorAll('#tum-tr')
tumTrAc.forEach((element) =>{
    element.addEventListener('click', () =>{
        const hamburgerMenuTumTr = document.querySelector('.hamburger-menu-tum-tr')
        hamburgerMenuTumTr.classList.toggle('hamburger-menu-aktif')
    });

    const ok = document.querySelectorAll('#ok-tum-tr')
    ok.forEach((e) => {
        e.addEventListener('click', ()=>{
            const hamburgerMenuTumTr = document.querySelector('.hamburger-menu-tum-tr')
            if(hamburgerMenuTumTr.classList.contains('hamburger-menu-aktif')){
            hamburgerMenuTumTr.classList.remove('hamburger-menu-aktif')
            }
        })
    })
});

// *Hesabım-Hamburger
const hesabimAc = document.querySelectorAll('#hesabim')
hesabimAc.forEach((element) =>{
    element.addEventListener('click', () =>{
        const hamburgerMenuHesabim = document.querySelector('.hamburger-menu-hesabim')
        hamburgerMenuHesabim.classList.toggle('hamburger-menu-aktif')
    });

    const ok = document.querySelectorAll('#ok-tum-tr')
    ok.forEach((e) => {
        e.addEventListener('click', ()=>{
            const hamburgerMenuTumTr = document.querySelector('.hamburger-menu-hesabim')
            if(hamburgerMenuTumTr.classList.contains('hamburger-menu-aktif')){
            hamburgerMenuTumTr.classList.remove('hamburger-menu-aktif')
            }
        })
    })
});
//!NAVBAR-HAMBURGER-MENU-END
//!NAVBAR-END


// HOTTICKETS-YENİ&YAKINDAGELECEKLER JS BAŞLANGIÇ KISMI 

let tikla = document.querySelector (".satis")
if (tikla)
{
tikla.addEventListener("click",
function ticketSatis(){
   
let hotSatis = document.querySelector (".satis")
hotSatis.style.border="2px solid #e6e6e6" 
hotSatis.style.borderBottom="none"  

let hotSatis2 = document.querySelector(".ticket")
hotSatis2.style.border="none"
hotSatis2.style.borderBottom="2px solid #e6e6e6"

let hotSatis3 = document.querySelector(".hottickettt")
hotSatis3.style.display = "none"

let hotSatis4 = document.querySelector(".yenisatisss")
hotSatis4.style.display="block"
}


)};


let tiklaa = document.querySelector(".ticket")
if (tiklaa) {
tiklaa.addEventListener("click",
function ticketSatis2(){


let hotSatis = document.querySelector (".ticket")
hotSatis.style.border="2px solid #e6e6e6" 
hotSatis.style.borderBottom="none"  

let hotSatis2 = document.querySelector(".satis")
hotSatis2.style.border="none"
hotSatis2.style.borderBottom="2px solid #e6e6e6"


let hotSatis3 = document.querySelector(".yenisatisss")
hotSatis3.style.display = "none"

let hotSatis4 = document.querySelector(".hottickettt")
hotSatis4.style.display="block"

}
)};


// HOTTICKETS-YENİ&YAKINDAGELECEKLER JS SON KISMI 


 // footer js start
        const acordionItems = document.querySelectorAll('.footer-main-acordion-item');
        // Html belgesinde footer-main-acordion-item sınıfına sahip tüm öğeleri seçer ve bu öğeleri acordionItem'a atar.

        acordionItems.forEach(item => {
            // acordionItems dizisindeki her bir akordion öğesi üzerinde bir döngü (forEach) başlatır.
            const header = item.querySelector('.footer-main-acordion-header');
            // her akordion öğesi içinde footer-main-acordion-header sınıfına sahip başlığı seçer ve header adlı bir değişkene atar.

            header.addEventListener('click', () => {
                // Her başlık öğesi için bir tıklama olay dinleyicisi ekler.
                item.classList.toggle('active');
                // Başlık öğesine tıklandığında, içeriğin açılmasını ve kapanmasını sağlayacak olan active sınıfını item adlı akordion öğesine ekleyip kaldırır. Yani, başlığa tıkladığınızda, active sınıfı eklenirse içerik görünür olacak, sınıf kaldırılırsa içerik gizlenecektir.


                acordionItems.forEach(otherItem => {
                    // Başlık öğesine tıklandığında, içeriğin açılmasını ve kapanmasını sağlayacak olan active sınıfını item adlı akordion öğesine ekleyip kaldırır. Yani, başlığa tıkladığınızda, active sınıfı eklenirse içerik görünür olacak, sınıf kaldırılırsa içerik gizlenecektir.
                    if (otherItem !== item) {
                        // Eğer mevcut otherItem akordion öğesi item akordion öğesi ile aynı değilse, yani seçilen akordionun dışındaki diğer öğelerse:
                        otherItem.classList.remove('active');
                        // sınıfını kaldırarak diğer akordion öğelerinin içeriğini kapatır.
                    }
                });
            });
        });
        const accordionHeaders = document.querySelectorAll('.footer-main-acordion-header');
        accordionHeaders.forEach(header => {
            header.addEventListener('click', function() {
                this.classList.toggle('active');
                // Başlık öğesine tıklandığında, içeriğin açılmasını ve kapanmasını sağlayacak olan active sınıfını başlık öğesine ekleyip kaldırır. Yani, başlığa tıkladığınızda, active sınıfı eklenirse içerik görünür olacak, sınıf kaldırılırsa içerik gizlenecektir.
            });
        });

        // footer js end


// muzik html sayfası
//  KATEGROİLER VE ETKİNLİK TARİHLERİ BAŞLANGIÇ
function gosterGizleMuzik(){
    let gizle = document.querySelector(".d2");
    let tiklad1 = document.querySelector(".d1");
    if(tiklad1){
       tiklad1.addEventListener("click", function () {
        let goster = document.querySelector(".d3");
        goster.classList.toggle("d3-active");
        tiklad1.style.display = "none";
        gizle.style.display = "block";
        }); 
    }    
    if(gizle){
        gizle.addEventListener("click", function () {
        gizle.style.display = "none";
        let goster = document.querySelector(".d3");
        goster.classList.remove("d3-active");
        tiklad1.style.display = "block";
        });
    }
}
gosterGizleMuzik()

//  KATEGROİLER VE ETKİNLİK TARİHLERİ BAŞLANGIÇ

// ETKİNLİK-LİSTE-JS-START
const sonuc = document.querySelector('#sonuc')
const divGoster = document.querySelector('.scriptgenel')
if(sonuc){
    sonuc.addEventListener('click', function(){
        divGoster.classList.toggle('scriptgenelactive')
    })
}

// ETKİNLİK-LİSTE-JS-END


/* (footer) Hesabım-(Hesap Oluştur ) createAccount.html START*/
 
  // tr tel no js start
  function TelephoneTr(){
  let telephone= document.getElementById("country-select")
  if(telephone){
    telephone.addEventListener("change", function() {
      var selectedValue = this.value;
      var phoneInput = document.getElementById("tr-tel");
  
      if (selectedValue === "90") {
          phoneInput.style.visibility = "visible";
      } else {
          phoneInput.style.visibility = "hidden";
      }
  });
  }
  }
  TelephoneTr();
//tr tel no js end

//modal box(1.checkbox'a basıldığında) start
function ModalHesapOlustur(){
var modalOlustur = document.getElementById("modalBoxForm");
var checkBoxHesap = document.getElementById("FirstCheckBox");
var modalKapa = document.getElementsByClassName("modal-kapa")[0];
var modalKapaİki = document.getElementsByClassName("modal-kapaiki")[0];
// checkbox'a tıkladığında aç
if(checkBoxHesap){
  checkBoxHesap.onclick = function() {
  modalOlustur.style.display = "block";
};
}
//modal dışında bir yere tıkladığında kapan
window.onclick = function(event) {
    if (event.target == modalOlustur) {
      modalOlustur.style.display = "none";
  }
};
//okudum anladım ve onaylamadan çık'a basınca kapan 
if(modalKapa){
  modalKapa.onclick = function() {
  modalOlustur.style.display = "none";
};
}
if(modalKapaİki){
  modalKapaİki.onclick = function() {
  modalOlustur.style.display = "none";
};
}
}
ModalHesapOlustur();
  ////modal box(1.checkbox'a basıldığında) end
// disable checkbox için start
    function disableOkudumCheck(){
    let checkboxOkudum = document.getElementById('okudumAnladim');
    let onaylamaButonu = document.getElementById('onaylamaButonu');

   if(onaylamaButonu){
    onaylamaButonu.addEventListener('click', () => {

      checkboxOkudum.disabled = false;
      checkboxOkudum.checked = true;
    });
  }
}
disableOkudumCheck();
// disable checkbox için end
/* (footer) Hesabım-account-(Hesap Oluştur ) createaccount.html  (hesabım sayfasının içinde bulunan sayfa) END  */

// (footer-bize ulaşın-contactus) contactus.html START

/*select'  -bize ulasin */ 
function contactInfo(){
const secili = document.getElementById("sec");
const ulasInfo = document.querySelectorAll(".ulas-info");

function update() {
  const seciliDeger = secili.value;
  ulasInfo.forEach(sec => {
    if (sec.id === seciliDeger + "Info") {
      sec.style.display = "block";
    } else {
      sec.style.display = "none";
    }
  });
}
  if (secili){
  secili.addEventListener("click", update);
}document.addEventListener("DOMContentLoaded", function () {
  const secili = document.getElementById("sec");
  const ulasInfo = document.querySelectorAll(".ulas-info");

  function update() {
      const seciliDeger = secili.value;
      ulasInfo.forEach(sec => {
          if (sec.id === seciliDeger + "Info") {
              sec.style.display = "block";
          } else {
              sec.style.display = "none";
          }
      });
  }

  if (secili) {
      secili.addEventListener("change", update); 
  }

  update(); // 
});
update();
contactInfo();
}

//(footer-bize ulaşın-contactus) contactus.html END


// ! ETKİNLİK-DETAY-BAŞLANGIÇ
// detay link 
// const clickableLink1 = document.getElementById('link1');
// const clickableLink2 = document.getElementById('link2');
// const clickableLink3 = document.getElementById('link3');
// const clickableLink4 = document.getElementById('link4');

// if (clickableLink1){
//     clickableLink1.addEventListener('click', function(){
//     clickableLink1.classList.add('etkinlik-detaylari-menu-aktif')
//     clickableLink2.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink3.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink4.classList.remove('etkinlik-detaylari-menu-aktif')
// });
// }
// if (clickableLink2)
// {
//     clickableLink2.addEventListener('click', function(){
//     clickableLink2.classList.add('etkinlik-detaylari-menu-aktif')
//     clickableLink1.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink3.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink4.classList.remove('etkinlik-detaylari-menu-aktif')
// });
// }
// if (clickableLink3)
// {
//     clickableLink3.addEventListener('click', function(){
//     clickableLink3.classList.add('etkinlik-detaylari-menu-aktif')
//     clickableLink1.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink2.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink4.classList.remove('etkinlik-detaylari-menu-aktif')
    
// });
// }
// if (clickableLink4)
// {
//     clickableLink4.addEventListener('click', function(){
//     clickableLink4.classList.add('etkinlik-detaylari-menu-aktif')
//     clickableLink1.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink2.classList.remove('etkinlik-detaylari-menu-aktif')
//     clickableLink3.classList.remove('etkinlik-detaylari-menu-aktif')
// });
// }

// bilet ücreti
// function updateSelects(){
//     var select1 = document.getElementById("select1");
//     var select2 = document.getElementById("select2");
//     var select3 = document.getElementById("select3");
//     var priceContent1=document.getElementById("ticket-price-content1");
//     var priceContent2=document.getElementById("ticket-price-content2");
//     var priceContent3=document.getElementById("ticket-price-content3");
//     if(select1){
//         if (select1.value === "1") {
//             select2.disabled = false;
//             select2.selectedIndex = 1;
//             select3.disabled = false;
//             select3.selectedIndex = 1;
//             priceContent1.style.display="none";
//             priceContent2.classList.add('dflex');
//             priceContent3.classList.remove('dflex');
//             // optionFirstic.classList.add('dblock');
//         } 
//         else if (select1.value === "2") {
//             select2.disabled = false;
//             select2.selectedIndex = 1;
//             select3.disabled = false;
//             select3.selectedIndex = 2;
//             priceContent1.style.display="none";
//             priceContent2.classList.remove('dflex');
//             priceContent3.classList.add('dflex');
//             if(select3.selectedIndex===2)
//             {
//                 console.log("tm")
//                 select3.selectedIndex[1].hide();
//             }
//         }
//     }  
// }
// Sayfa yüklendiğinde veya güncellendiğinde seçimleri kontrol etmek için
// window.onload = updateSelects;

  
const toggleBtnPaylas = document.getElementById("toggleBtn-1");
const menuPaylas = document.getElementById("menuPaylas-detay");
if(toggleBtnPaylas)
{
    toggleBtnPaylas.addEventListener("click", () => {
    menuPaylas.classList.toggle("paylas-active");
});

}
// ! ETKİNLİK-DETAY-BİTİŞ

// SÖZLEŞME  BAŞLANGIÇ

let aktifDiva1 = null;
function linkMen(link){
    const linkGrupId = link.dataset.target;
    const linkGrup = document.getElementById(linkGrupId);
    console.log(linkGrup)
    if (aktifDiva1 !== null && aktifDiva1 !== linkGrup) {
        aktifDiva1.style.display = "none";
    }
    linkGrup.style.display = linkGrup.style.display === "block" ? "none" : "block";
    aktifDiva1 = linkGrup.style.display === "block" ? linkGrup : null;
}

// SÖZLEŞME BİTİŞ

// ALED-BURCU SON JS BAŞLANGIÇ
//! SCROLL BAR

const categoryScroller = document.getElementById("categoryScroller");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const scrollAmount = 300; // Kaydırma miktarı (px)

// Kategori carousel'ını başlangıçta odalar kategorisiyle başlatmak için aşağıdaki kodu ekleyin:
if(categoryScroller){
    categoryScroller.scrollLeft = 0;
}

if (prevBtn) {
  

prevBtn.addEventListener("click", () => {
  categoryScroller.scrollLeft -= scrollAmount;
  if (categoryScroller.scrollLeft < 0) {
    categoryScroller.scrollLeft = 0;
  }
});
}
if (nextBtn) {
  
nextBtn.addEventListener("click", () => {
  categoryScroller.scrollLeft += scrollAmount;
  if (
    categoryScroller.scrollLeft >
    categoryScroller.scrollWidth - categoryScroller.clientWidth
  ) {
    categoryScroller.scrollLeft =
      categoryScroller.scrollWidth - categoryScroller.clientWidth;
  }
});
}

const categoryScrollerr = document.getElementById("categoryScroller-2");
const prevBtnn = document.getElementById("prevBtn-2");
const nextBtnn = document.getElementById("nextBtn-2");
const scrollAmountt = 300; // Kaydırma miktarı (px)

// Kategori carousel'ını başlangıçta odalar kategorisiyle başlatmak için aşağıdaki kodu ekleyin:
if(categoryScroller){
    categoryScroller.scrollLeft = 0;
}

if(prevBtnn){

prevBtnn.addEventListener("click", () => {
  categoryScrollerr.scrollLeft -= scrollAmount;
  if (categoryScrollerr.scrollLeft < 0) {
    categoryScrollerr.scrollLeft = 0;
  }
});
}

if (nextBtnn) {
  
nextBtnn.addEventListener("click", () => {
  categoryScrollerr.scrollLeft += scrollAmount;
  if (
    categoryScrollerr.scrollLeft >
    categoryScrollerr.scrollWidth - categoryScrollerr.clientWidth
  ) {
    categoryScroller.scrollLeft =
      categoryScrollerr.scrollWidth - categoryScrollerr.clientWidth;
  }
});
}

//! Şifre değiştirme js

const newPasswordInput = document.getElementById("newPassword");
const confirmNewPasswordInput = document.getElementById("confirmNewPassword");
const requirements = document.querySelectorAll(".sifreOzellikleri p i");
const formInputs = document.querySelectorAll(".form-control");
const updateButton = document.getElementById("updateButton");
const passwordMismatchError = document.getElementById("passwordMismatchError");

if (newPasswordInput) {
  newPasswordInput.addEventListener("input", function () {
  const password = this.value;

  const hasMinimumLength = password.length >= 8;
  const hasLetter = /[a-zA-Z]/.test(password);
  const hasDigitOrSpecialChar = /[0-9!@#$%^&*()_+[\]{};':"\\|,.<>?]/.test(
    password
  );

  updateRequirement(requirements[0], hasMinimumLength);
  updateRequirement(requirements[1], hasLetter);
  updateRequirement(requirements[2], hasDigitOrSpecialChar);

  const isValid = hasMinimumLength && hasLetter && hasDigitOrSpecialChar;
  const formContainer = document.querySelector(".sifreDegistir");
  formContainer.classList.toggle("valid", isValid);
  });
}

if (confirmNewPasswordInput) {
  
confirmNewPasswordInput.addEventListener("input", function () {
  const newPassword = newPasswordInput.value;
  const confirmNewPassword = confirmNewPasswordInput.value;

  if (confirmNewPassword === newPassword) {
    confirmNewPasswordInput.classList.remove("error-input");
    passwordMismatchError.style.display = "none";
  } else {
    confirmNewPasswordInput.classList.add("error-input");
    passwordMismatchError.style.display = "block";
  }
});
}

function updateRequirement(requirementElement, isFulfilled) {
  const icon = requirementElement;
  icon.classList.toggle("fa-check-circle", isFulfilled);
  icon.classList.toggle("fa-circle-xmark", !isFulfilled);
  icon.style.color = isFulfilled ? "green" : "gray";
}

formInputs.forEach((input) => {
  input.addEventListener("input", function () {
    if (this.classList.contains("error-input")) {
      this.classList.remove("error-input");
    }
    if (this.value === "") {
      this.classList.add("error-input");
    }
  });
});

if(updateButton){

updateButton.addEventListener("click", function (event) {
  formInputs.forEach((input) => {
    if (input.value === "") {
      input.classList.add("error-input");
      event.preventDefault();
    }
  });

  if (newPasswordInput.value !== confirmNewPasswordInput.value) {
    confirmNewPasswordInput.classList.add("error-input");
    passwordMismatchError.style.display = "block";
    event.preventDefault();
  }
});
}

//! Bireysel ve Kurumsal Fatura
const buttons = document.querySelectorAll(".button-section");
const bireyselFatura = document.querySelector(".bireyselFatura");
const kurumsalFatura = document.querySelector(".kurumsalFatura");

// İlk yüklendiğinde Bireysel seçili olarak ayarla
// bireyselFatura.style.display = "flex";
// kurumsalFatura.style.display = "none";

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    buttons.forEach((btn) => btn.classList.remove("selected"));
    button.classList.add("selected");

    if (button.id === "bireysel") {
      bireyselFatura.style.display = "flex";
      kurumsalFatura.style.display = "none";
    } else if (button.id === "kurumsal") {
      bireyselFatura.style.display = "none";
      kurumsalFatura.style.display = "flex";
    }
  });
});

//! HOOVER ÖZELLİKLERİ

let biletEtkinliklinkss = document.querySelectorAll(".biletlerimEtkinlikHvr");

biletEtkinliklinkss.forEach((etkinlikLink) => {
  etkinlikLink.addEventListener("click", () => {
    const linkId = etkinlikLink.getAttribute("data-id");

    biletEtkinliklinkss.forEach((l) => {
      if (l.getAttribute("data-id") === linkId) {
        l.classList.toggle("active");
      } else {
        l.classList.remove("active");
      }
    });
  });
});


let basss = document.querySelector(".hesapAyarlariB");
if (basss) {
basss.addEventListener("click",
function hesapAyari(){


let hesapAyarlari = document.querySelector (".hessap")
hesapAyarlari.style.display = "block";

let hesapAyarlari2 = document.querySelector (".biletlerimBilgisag")
hesapAyarlari2.style.display = "none";


}
)};

let bass = document.querySelector(".biletlerimmm");
if (bass) {
bass.addEventListener("click",
function hesapAyarii(){


let hesapAyarlari4 = document.querySelector (".biletlerimBilgisag")
hesapAyarlari4.style.display = "block";

let hesapAyarlari3 = document.querySelector (".hessap")
hesapAyarlari3.style.display = "none";


}
)};


// ALED-BURCU SON JS SONU

//dolusepet.html START

// koltuk bilgilerini gör js (sepet) 

function bilgiKoltuk(){
  let biletBilgi= document.getElementById("ticketInfo")
  if (biletBilgi){
  biletBilgi.addEventListener("click", function() {
      var biletHidden = document.getElementById("biletHidden");
  
      if (biletHidden.classList.contains("d-none")) {
        biletHidden.classList.remove("d-none");
      } else {
        biletHidden.classList.add("d-none");
      }
    });
  }
   }
   bilgiKoltuk()
  
    // koltuk bilgilerini gör js (sepet) end
    
    //koltuk bilgilerini gör 950px responsive de çıkan için  start
  function koltukBilgi(){
    let biletBilgiİki= document.getElementById("ticketInfo2")
  if (biletBilgiİki){
    biletBilgiİki.addEventListener("click", function() {
      var biletHiddenİki = document.getElementById("biletHiddenİki");
  
      if (biletHiddenİki.classList.contains("d-none")) {
        biletHiddenİki.classList.remove("d-none");
      } else {
        biletHiddenİki.classList.add("d-none");
      }
    });
  }
  }
  koltukBilgi()
    //koltuk bilgilerini gör 950px responsive de çıkan için  end
  
    // dolu sepet modal start
    function BtnIcon(){
    var sepetModalBox = document.getElementById("sepetModal");
    var ModalBoxBtn = document.getElementById("sepetModalBoxBtn");
    var sepetModalKapanBir = document.getElementsByClassName("sepetModalKapan")[0];
    // buton-icona tıkladığında tıkladığında aç
    if(ModalBoxBtn){
      ModalBoxBtn.onclick = function() {
      sepetModalBox.style.display = "block";
    }
    }
    //modal dışında bir yere tıkladığında kapan
    window.onclick = function(event) {
      if (event.target == sepetModalBox) {
        sepetModalBox.style.display = "none";
      }
    }
    //X'e bastığında kapan
    if(sepetModalKapanBir){
      sepetModalKapanBir.onclick = function() {
        sepetModalBox.style.display = "none";
      }
    }

    }
    BtnIcon()
      // dolu sepet modal end
     
      //dolusepet.html END
// !HEDİYE-KART-START
function MoreLess(){
  var dots= document.getElementById("dots");
  var invisibleText = document.getElementById("invisible-text");
  var btnText = document.getElementById("btn");
  if(dots.style.display!="none"){
      dots.style.display="none";
      invisibleText.style.display= "inline";
      btnText.innerHTML= "Gizle";
  }
  else{
      dots.style.display="inline";
      invisibleText.style.display= "none";
      btnText.innerHTML= "Devamını Oku";

  }
}
function MoreLess1(){
  var dots= document.getElementById("dots");
  var invisibleText1 = document.getElementById("invisible-text1");
  var btn1Text = document.getElementById("btn1");
  if(dots.style.display!="none"){
      dots.style.display="none";
      invisibleText1.style.display= "inline";
      btn1Text.innerHTML= "Gizle";
  }
  else{
      dots.style.display="inline";
      invisibleText1.style.display= "none";
      btn1Text.innerHTML= "Devamını Oku";

  }
}

function MoreLesss(){
  var dots= document.getElementById("dots");
  var invisibleText2 = document.getElementById("invisible-text2");
  var btnmekanText = document.getElementById("btnmekan");
  if(dots.style.display!="none"){
      dots.style.display="none";
      invisibleText2.style.display= "inline";
      btnmekanText.innerHTML= "Gizle";
  }
  else{
      dots.style.display="inline";
      invisibleText2.style.display= "none";
      btnmekanText.innerHTML= "Daha Fazla Göster";

  }
}
// !HEDİYE-KART-END