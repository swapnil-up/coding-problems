package Kyu7

object Solution {

    fun nameValue(arr: Array<String>): IntArray {
        var a= mutableListOf<Int>()
        for (i in 0..arr.size-1){
            var item=arr[i].toCharArray()
            var sum=0
            for (j in 0..item.size-1){
                if (item[j]==' ') continue
                else sum+= item[j].code - 'a'.code +1
            }
            a.add(sum*(i+1))
        }
        return a.toIntArray()
    }

}

fun main() {
    val result1 = Solution.nameValue(arrayOf("abc", "abc abc"))
    val result2 = Solution.nameValue(arrayOf("codewars", "abc", "xyz"))
    val result3 = Solution.nameValue(arrayOf("abcdefghijklmnopqrstuvwxyz", "stamford bridge", "haskellers"))

    println(result1.joinToString(", ")) // Print the result as a comma-separated string
    println(result2.joinToString(", "))
    println(result3.joinToString(", "))
}