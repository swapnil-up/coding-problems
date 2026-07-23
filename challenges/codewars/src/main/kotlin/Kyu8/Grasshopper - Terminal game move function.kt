package Kyu8

fun move(pos: Int, roll: Int): Int {
    return (roll*2+pos)
}

fun main() {
    println(move(0, 4))
    println(move(3, 6))
    println(move(2, 5))
}