package Kyu7

fun findShort(s: String): Int {
    var words=s.split(" ")
    var count=words[0].count()
    for(i in words.indices){
        if (count>words[i].count()) count=words[i].count()
    }
    return count
}

fun main() {
    println(findShort("bitcoin take over the world maybe who knows perhaps"))
    println(findShort("turns out random test cases are easier than writing out basic ones"))
    println(findShort("Let's travel abroad shall we"))
}