package unsolved

object Kata {
    fun digitize(n: Long): IntArray {
        val numString = n.toString()
        val reversedArray = IntArray(numString.length)

        for (i in numString.indices) {
            reversedArray[i] = numString[numString.length - 1 - i].toString().toInt()
        }

        return reversedArray
    }

}


fun main() {
    println(Kata.digitize(35231))
    println(Kata.digitize(0))
}