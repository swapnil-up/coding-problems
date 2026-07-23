package Kyu8

fun litres(time: Double): Int {
    return(0.5*time).toInt()
}

fun main() {
    println(litres(2.0))
    println(litres(1.4))
    println(litres(12.3))
//    assertEquals(0, litres(0.82))
//    assertEquals(5, litres(11.8))
    println(litres(1787.0))
//    assertEquals(0, litres(0.0))
}