
$('#add-income').click(function(){
  $('#income-modal').css('display', 'block');
  console.log("I was clicked")
})

$('#add-bill').on('click', () => {
    $('#bill-modal').css('display', 'block');
    console.log("I was clicked bill");
    console.log("I was clicked bill 222");
    console.log($('#bill-modal'), 'bill modal');
  })

let addBudgetBtn = document.getElementById("add-budget")
addBudgetBtn.addEventListener('click', function(){
  console.log("add budget was pressed")
})


let addBillBtn = document.getElementById("add-bill")
addBudgetBtn.addEventListener('click', function(){
  console.log("add bill was pressed")
})