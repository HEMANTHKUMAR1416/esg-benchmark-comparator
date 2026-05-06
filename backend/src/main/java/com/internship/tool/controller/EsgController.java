package com.internship.tool.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/esg")
@CrossOrigin(origins = "*")
public class EsgController {

    @PostMapping("/describe")
    public ResponseEntity<Map<String, Object>> describe(@RequestBody Map<String, Object> request) {

        String company = request.get("company_name").toString();

        int env = Integer.parseInt(request.get("env_score").toString());
        int social = Integer.parseInt(request.get("social_score").toString());
        int gov = Integer.parseInt(request.get("gov_score").toString());

        int average = (env + social + gov) / 3;

        Map<String, Object> response = new HashMap<>();

        response.put("company", company);
        response.put("average_score", average);

        if (average >= 75) {
            response.put("description", company + " demonstrates strong ESG performance.");
        } else if (average >= 50) {
            response.put("description", company + " shows moderate ESG performance with room for improvement.");
        } else {
            response.put("description", company + " has weak ESG performance and requires significant improvements.");
        }

        return ResponseEntity.ok(response);
    }

    @PostMapping("/recommend")
    public ResponseEntity<Map<String, Object>> recommend(@RequestBody Map<String, Object> request) {

        int env = Integer.parseInt(request.get("env_score").toString());
        int social = Integer.parseInt(request.get("social_score").toString());
        int gov = Integer.parseInt(request.get("gov_score").toString());

        Map<String, Object> response = new HashMap<>();

        if (env < 70) {
            response.put("environment_recommendation",
                    "Improve renewable energy adoption and reduce emissions.");
        }

        if (social < 70) {
            response.put("social_recommendation",
                    "Enhance employee welfare and community engagement.");
        }

        if (gov < 70) {
            response.put("governance_recommendation",
                    "Strengthen transparency and compliance policies.");
        }

        response.put("status", "Recommendations generated successfully");

        return ResponseEntity.ok(response);
    }
}