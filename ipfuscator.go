package main

import (
	"flag"
	"fmt"
	"math/rand"
	"regexp"
	"strconv"
	"strings"
	"time"
)

var version = "1.0.0"

func main() {
	ipPtr := flag.String("ip", "", "The IP to perform IPFuscation on")
	flag.Parse()
	if *ipPtr == "" {
		fmt.Println("Please specify ip using -ip flag.")
		return
	}

	showBanner()
	ip := *ipPtr
	if checkIP(ip) {
		fmt.Printf("\nIP address: \t%s", ip)
		printOutput(ip)
	} else {
		fmt.Printf("[!] Invalid IP format: %s\n", ip)
	}
}

func showBanner() {
	fmt.Println("IPFuscator")
	fmt.Println("Author: Vincent Yiu (@vysecurity)")
	fmt.Println("https://www.github.com/vysecurity/IPFuscator")
	fmt.Printf("Version: %s\n", version)
	fmt.Println()
}

func checkIP(ip string) bool {
	match, _ := regexp.MatchString(`(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})`, ip)
	if match {
		parts := strings.Split(ip, ".")
		if len(parts) == 4 {
			for _, p := range parts {
				if num, err := strconv.Atoi(p); err != nil || num < 0 || num > 255 {
					return false
				}
			}
			return true
		}
	}
	return false
}

func printOutput(ip string) {
	parts := strings.Split(ip, ".")

	dec := [4]int{}
	hex := [4]string{}
	oct := [4]string{}
	for i := 0; i < 4; i++ {
		dec[i], _ = strconv.Atoi(parts[i])
		hex[i] = strconv.FormatInt(int64(dec[i]), 16)
		oct[i] = strconv.FormatInt(int64(dec[i]), 8)
	}

	decimal := dec[0]*16777216 + dec[1]*65536 + dec[2]*256 + dec[3]
	fmt.Printf("\nDecimal:\t%d", decimal)
	fmt.Printf("\nHexadecimal:\t%x", decimal)
	fmt.Printf("\nOctal:\t\t%o", decimal)

	fmt.Printf("\n\nFull Hex:\t%s", strings.Join(hex[:], "."))
	fmt.Printf("\nFull Oct:\t%s", strings.Join(oct[:], "."))

	fmt.Println("\n\nRandom Padding: ")

	rand.Seed(time.Now().UnixNano())
	randhex := [4]string{}
	randoct := [4]string{}
	for i := 0; i < 4; i++ {
		randhex[i] = fmt.Sprintf("%x", dec[i]*int(rand.Intn(30)+1))
		randoct[i] = fmt.Sprintf("%o", dec[i]*int(rand.Intn(30)+1))
	}

	fmt.Printf("\nHex:\t\t%s", strings.Join(randhex[:], "."))
	fmt.Printf("\nOct:\t\t%s", strings.Join(randoct[:], "."))

	fmt.Println("\n\nRandom base:")
	for i := 0; i < 5; i++ {
		randbase := [4]string{}
		for j := 0; j < 4; j++ {
			choices := [3]string{parts[j], hex[j], oct[j]}
			randbase[j] = choices[rand.Intn(3)]
		}
		fmt.Printf("\n#%d:\t\t%s", i+1, strings.Join(randbase[:], "."))
	}

	fmt.Println("\n\nRandom base with random padding:")
	for i := 0; i < 5; i++ {
		randbase := [4]string{}
		for j := 0; j < 4; j++ {
			switch rand.Intn(3) {
			case 0:
				randbase[j] = parts[j]
			case 1:
				randbase[j] = fmt.Sprintf("%x",
					dec[j]*int(rand.Intn(30)+1))
			default:
				randbase[j] = fmt.Sprintf("%o",
					dec[j]*int(rand.Intn(30)+1))
			}
		}
		fmt.Printf("\n#%d:\t\t%s", i+1, strings.Join(randbase[:], "."))
	}
	fmt.Println()
}