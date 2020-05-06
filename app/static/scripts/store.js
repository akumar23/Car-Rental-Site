(function(){
  const cartInfo = document.getElementbyID('cartInfo');
  const cart = document.getElementbyID('cart');

  cartInfo.addEventListener('click', function(){
    cart.classList.toggle("show-cart");
  });
})();

(function(){
  const checkoutButton = document.querySelectorAll('.carIcon')
  checkoutButton.forEach(function(btn){
    btn.addEventListener('click',function(event){
      //console.log(event.target);

      if(event.target.parentElement.classList.contains("carIcon")){
        let fullPath = event.target.parentElement.previousElementSibling.src;
        let position = fullPath.indexOf('pictures')+8;
        let picPath = fullPath.slice(position);

        const item = {};
        item.img = 'cart-img${picPath}';
        let name = event.target.parentElement.parentElement.nextElementSibling.children[0].children[0].textContent;
      }
    })
  })
})();
