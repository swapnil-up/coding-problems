package Kyu7

object FixStringCase {

    fun solve(s: String): String {
        var up=0
        var low=0
        for (i in 0..s.length-1){
            if (s[i] in 'a'..'z') low+=1
            if(s[i] in 'A'..'Z') up+=1
        }
        if (low>=up) return (s.lowercase()) else return s.uppercase()
    }

}

fun main() {
    println(FixStringCase.solve("code"))
    println(FixStringCase.solve("CODe"))
    println(FixStringCase.solve("COde"))
    println(FixStringCase.solve("Code"))
    println(FixStringCase.solve(""))
}