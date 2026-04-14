#creating a reporting system that would generate reports in JSON, CSV, and HTML formats with export functionality 
import json
import csv
import os
from io import StringIO
from datetime import datetime
from .vulnerability import Vulnerability

class ReportGenerator:
    def __init__(self,vulenrabilities, title="CodeRisk Report"):
        self.vulnerabilities = vulnerabilities
        self.title = title
        self.generated_at = datetime.utcnow().isoformat() + "Z"
    
    def generate_json(self, include_stats=False):
        report = {
            "title": self.title,
            "generated_at": self.generated_at,
            "vulnerabilities": [vuln.__dict__ for vuln in self.vulnerabilities]
        }
        if include_stats:
            report["statistics"] = self._generate_statistics()
            return json.dumps(report, indent=2)
        return json.dumps(report, indent=2)
    
    def generate_csv(self):
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Tool", "File", "Line", "Severity", "Description"])
        for vuln in self.vulnerabilities:
            writer.writerow([vuln.tool, vuln.file, vuln.line, vuln.severity, vuln.description])
            return output.getvalue()
        
    def generate_html(self, include_stats=False):
        html = f"<html><head><title>{self.title}</title></head><body>"
        html += f"<h1>{self.title}</h1>"
        html += f"<p>Generated at: {self.generated_at}</p>"
        if include_stats:
            stats = self._generate_statistics()
            html += "<h2>Statistics</h2><ul>"
            for key, value in stats.items():
                html += f"<li>{key}: {value}</li>"
                html += "</ul>"
                html += "<h2>Vulnerabilities</h2><table border='1'><thead><tr><th>Tool</th><th>File</th><th>Line</th><th>Severity</th><th>Description</th></tr></thead><tbody>"
            
            for vuln in self.vulnerabilities:
                html += f"<tr><td>{vuln.tool}</td><td>{vuln.file}</td><td>{vuln.line}</td><td>{vuln.severity}</td><td>{vuln.description}</td></tr>"
                html += "</tbody></table>"
                return html
    def