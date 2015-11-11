package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
	"encoding/json"
)

func elRequest(url string,data string)(string) {
	fmt.Println("The elastic search URL:>", url)
	var query = []byte(data)
	
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(query))
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	fmt.Println("response Status:", resp.Status)
	fmt.Println("response Headers:", resp.Header)
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println("response Body:", string(body))
	return string(body)
}

func parseReqBodyToJson(r *http.Request) map[string]interface{} {
	result, _ := ioutil.ReadAll(r.Body)
	defer r.Body.Close()
	var f interface{}
	err := json.Unmarshal(result, &f)
	if err != nil {		
		panic(err)
	}
	return f.(map[string]interface{})
}

func elHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method == "POST" {
		payload := parseReqBodyToJson(r)
        url := payload["url"].(string)
        query := payload["query"].(string)
        result := elRequest(url,query)
        w.Header().Set("content-type", "application/json")
        w.Write([]byte(result))
    }
}

func main(){
    http.Handle("/", http.FileServer(http.Dir("public")))
    http.HandleFunc("/elsearch",elHandler)
    http.ListenAndServe(":8888", nil)    
}
