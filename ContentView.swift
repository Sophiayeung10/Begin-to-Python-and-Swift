//
//  ContentView.swift
//  Xcode Tutorial Demo
//
//  Created by Hiu Wai Yeung on 8/21/24.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        // Vertical Stack layout
        VStack {
        // image
            Image("selfie")
                .resizable()
                .padding(.top, 2.0)
                .frame(width: 300, height: 500)
                .cornerRadius(20)
                .imageScale(.large)
                .foregroundStyle(.tint)
        // text on the app
            Text("Sophia Yeung")
                .foregroundColor(.black)
                .bold()
                .padding()
            Button("Instagram") {
                print("hiuwaiyeung10")
        /*
         this is the button for clicking to see my instagram account
        */
                
            
            }
            
                }
            }

            
        }

    


#Preview {
    ContentView()
}
