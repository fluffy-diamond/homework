function hi() {
  var number = " "
        for (i = 1; i < 11; i++) {
            number += " <br> ";
        }
        document.write("The random value is " + Math.floor(Math.random() * 100) + "<br>");
        var date = new Date();
        document.write("Today's Date is " + date.getDate());
}