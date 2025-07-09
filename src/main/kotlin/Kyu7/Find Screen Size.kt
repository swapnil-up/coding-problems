package Kyu7

import kotlin.time.times

fun findScreenHeight(width: Int, ratio: String): String {
    var array=ratio.split(":")
    var result=width*array.last().toInt()/array.first().toInt()
    return "$width"+"x"+"$result"
}

fun main() {
    println(findScreenHeight(1024,"4:3"))
    println(findScreenHeight(1280,"16:9"))
    println(findScreenHeight(3840,"32:9"))
}