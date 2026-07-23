package Kyu8

fun replace(s: String): String = s.replace(Regex("[aeiouAEIOU]"),"!")

fun main() {
    println(replace("Hi!"))
    println(replace("!Hi! Hi!"))
    println(replace("aeiou"))
    println(replace("ABCDE"))
}