document.querySelectorAll('.track').forEach(item => {
  item.addEventListener('click', event => {
  	var trackname=item.getAttribute('trackname');
    console.log(mixpanel)
  })
})