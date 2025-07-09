package Kyu7

import kotlin.math.abs

fun mxdiflg(a1:Array<String>, a2:Array<String>):Int {
    var max=-1
    for (i in 0..a1.size-1){
        for (j in 0..a2.size-1){
            if (abs(a1[i].length-a2[j].length)>max) max= abs(a1[i].length-a2[j].length)
            if (abs(a2[j].length-a1[i].length)>max) max= abs(a2[i].length-a1[j].length)
        }
    }
    return max
}

fun main() {
    println("mxdiflg Fixed Tests")
    var s1 = arrayOf<String>("hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz")
    var s2 = arrayOf<String>("cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww")
    println(mxdiflg(s1, s2))
    s1 = arrayOf<String>("ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh")
    s2 = arrayOf<String>("bbbaaayddqbbrrrv")
    println(mxdiflg(s1, s2))

}