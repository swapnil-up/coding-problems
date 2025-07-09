package Kyu6

fun high(str: String) : String {
    var arrayWords=str.split(" ")
    var max=0
    var result=""
    for (i in 0..arrayWords.count()-1){
        var pointWord=arrayWords[i]
        var points=0
        for (i in 0..pointWord.count()-1){
            points+= pointWord[i].code-'a'.code+1
        }
        if (points>max) {
            result=pointWord
            max=points
        }
    }
    return result
}

fun main() {
    println(high("man i need a taxi up to ubud"))
    println(high("what time are we climbing up the volcano"))
    println(high("take me to semynak"))
    println(high("aa b"))
    println(high("b aa"))
    println(high("bb d"))
    println(high("d bb"))
    println(high("aaa b"))
}