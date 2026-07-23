package Kyu8

fun opposite(number: Int): Int {
    return (-2*number+number)
}

fun main() {
    println(opposite(1));
    println(opposite(0));
    println(opposite(-25));
}