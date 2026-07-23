package Kyu7

fun seven(n:Long):LongArray {
    var rem=n
    var c:Long=0
    while (rem>99) {
        val last=rem%10
        rem=(rem/10) - (2*last)
        c++
    }
    return longArrayOf(rem,c)
}

fun main() {
    val result1 = seven(286)
    println("Result for 371: [${result1[0]}, ${result1[1]}]")

    val result2 = seven(1603)
    println("Result for 1603: [${result2[0]}, ${result2[1]}]")
}
