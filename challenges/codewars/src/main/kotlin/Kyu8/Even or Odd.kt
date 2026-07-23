package Kyu8

fun evenOrOdd(number: Int): String {
    if(number%2==0) return("Even") else return("Odd")
}
fun testFixed() {
    println(evenOrOdd(2))
    println(evenOrOdd(0))
    println(evenOrOdd(7))
    println(evenOrOdd(1))
}