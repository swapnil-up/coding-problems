package Kyu7

object Opstrings {

    fun vertMirror(strng: String): String {
        var segments=strng.split("\n")
        var reversed=segments.map{it.reversed()}
        var result=reversed.joinToString("\n") { it }
        return result
    }
    fun horMirror(strng: String): String {
        var segments=strng.split("\n")
        var reversed=segments.asReversed()
        var result=reversed.joinToString("\n") { it }
        return result
    }
    fun oper(func:(String)->String, s: String): String {
        return(func(s))
    }
}

fun main() {
    val o = Opstrings

    println("Vertical Mirror:")
    val verticalInput = "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"
    val verticalResult = o.oper(o::vertMirror, verticalInput)
    println(verticalResult)

    println("Horizontal Mirror:")
    val horizontalInput = "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"
    val horizontalResult = o.oper(o::horMirror,horizontalInput)
    println(horizontalResult)
}
