fun billboard(name:String,price:Int = 30){
    var value=0
    var count=name.count()
    for(i in 1..count) {value+=price}
    println(value)
}


fun main(){
    billboard("Jeong-Ho Aristotelis")
    billboard("Abishai Charalampos")
    billboard("Idwal Augustin")
    billboard("Hadufuns John",20)
    billboard("Zoroaster Donnchadh")
//    Test.assertEquals(billboard("Claude Miljenko"), 450);
//    Test.assertEquals(billboard("Werner Vígi",15), 165);
//    Test.assertEquals(billboard("Anani Fridumar"), 420);
//    Test.assertEquals(billboard("Paolo Oli"), 270);
//    Test.assertEquals(billboard("Hjalmar Liupold",40), 600);
//    Test.assertEquals(billboard("Simon Eadwulf"), 390);
}