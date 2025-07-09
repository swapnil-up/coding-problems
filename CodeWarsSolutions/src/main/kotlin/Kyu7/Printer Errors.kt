package Kyu7

fun printerError(s: String): String {
    var errorCount=0
    for(i in 0..s.length-1){
        if (s[i] in 'n'..'z') errorCount+=1
    }
    return errorCount.toString()+"/${s.count()}"
}

fun main() {
    println(printerError("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
    println(printerError("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
    println(printerError("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"))
    println(printerError("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmm"))
}