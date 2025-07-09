package Kyu7

fun makeComplement(dna : String) : String {
    var replaced=""
    for(i in 0..<dna.length){
        if (dna[i]=='A') replaced+='T'
        else if (dna[i]=='T') replaced+='A'
        else if (dna[i]=='G') replaced+='C'
        else if (dna[i]=='C') replaced+='G'
    }
    return replaced
}

fun main() {
    println(makeComplement("AAAA"))
    println(makeComplement("ATTGC"))
}