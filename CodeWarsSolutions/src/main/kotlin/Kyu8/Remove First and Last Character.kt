package Kyu8

fun removeChar(str: String): String {
    return str.subSequence(1..str.length-2).toString()
}

fun main() {
    println(removeChar("eloquent"))
    println(removeChar("country"))
    println(removeChar("person"))
    println(removeChar("place"))
}