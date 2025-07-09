package Kyu7

fun reverseLetter(str: String): String {
    var rev=""
    for(i in 0 .. str.count()-1){
        if(str[i] in 'A'..'Z' || str[i] in 'a'..'z') rev=str[i]+rev
    }
    return rev
}

fun main() {
    println(reverseLetter("krishan"))
    println(reverseLetter("ultr53o?n"))
    println(reverseLetter("ab23c"))
    println(reverseLetter("krish21an"))
}