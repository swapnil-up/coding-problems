package Kyu8

fun noSpace(x: String): String {
    return (x.replace(" ",""))
}

fun main() {
    println(noSpace("8 j 8   mBliB8g  imjB8B8  jl  B"))
    println(noSpace("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))
    println(noSpace("8aaaaa dddd r     "))
}