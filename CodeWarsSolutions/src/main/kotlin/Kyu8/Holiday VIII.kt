package Kyu8

fun dutyFree(normPrice: Int, discount:Int, hol:Int) : Int {
    var discountAmount=normPrice*((discount*0.01).toFloat())
    return((hol/discountAmount).toInt())
}

fun main() {
    println(dutyFree(12, 50, 1000))
    println(dutyFree(17, 10, 500))
    println(dutyFree(24, 35, 3000))
    println(dutyFree(377, 40, 9048))
    println(dutyFree(2479, 51, 13390))
}