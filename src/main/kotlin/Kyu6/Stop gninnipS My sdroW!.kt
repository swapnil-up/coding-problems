package Kyu6

fun spinWords(sentence: String): String {
    var stringArray= sentence.split(" ").toMutableList()
    for(i in 0..<stringArray.count()){
        if (stringArray[i].count()>4) stringArray[i]=stringArray[i].reversed()
    }
    return stringArray.joinToString(" ")
}
fun main() {
    println(spinWords("Welcome"))
    println(spinWords("Hey fellow warriors"))
    println(spinWords("This is a test"))
    println(spinWords("This is another test"))
    println(spinWords("You are almost to the last test"))
    println(spinWords("Just kidding there is still one more"))
}

