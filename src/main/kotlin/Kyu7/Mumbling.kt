package Kyu7

fun accum(s:String):String {
    var accum=""
    for(i in 0..<s.length){
        for(j in 0..i){
            if(j==0) accum+=s[i].uppercase()
            else accum+=s[i].lowercase()
        }
        if(i!=s.length-1) accum+="-"
    }
    return accum
}

fun main() {
    println("Fixed Tests accum")
    println(accum("ZpglnRxqenU"))
    println(accum("NyffsGeyylB"))

}