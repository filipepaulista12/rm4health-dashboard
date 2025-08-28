"""
RM4Health Analytics Module
Módulo de análises avançadas para o dashboard REDCap
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re
from collections import Counter, defaultdict

class RM4HealthAnalytics:
    def __init__(self, data):
        self.data = data if data else []
        self.processed_data = self.data.copy()
    
    def analyze_longitudinal_data(self):
        """Análise longitudinal dos dados"""
        if not self.data:
            return {'message': 'Nenhum dado disponível', 'participants': []}
        
        # Agrupar por participante
        participant_data = defaultdict(list)
        for record in self.data:
            participant_id = record.get('participant_id', record.get('record_id', 'unknown'))
            participant_data[participant_id].append(record)
        
        analysis = {
            'total_participants': len(participant_data),
            'participants': []
        }
        
        for participant_id, records in participant_data.items():
            participant_analysis = {
                'id': participant_id,
                'total_records': len(records),
                'date_range': self._get_date_range(records),
                'trends': self._analyze_trends(records)
            }
            analysis['participants'].append(participant_analysis)
        
        return analysis
    
    def analyze_healthcare_utilization(self):
        """Análise de utilização de cuidados de saúde"""
        if not self.data:
            return {'message': 'Nenhum dado disponível'}
        
        healthcare_fields = [
            'healthcare_visits', 'emergency_visits', 'hospitalizations',
            'specialist_visits', 'primary_care_visits', 'medication_changes'
        ]
        
        utilization_stats = {}
        for field in healthcare_fields:
            values = [record.get(field) for record in self.data if record.get(field)]
            if values:
                utilization_stats[field] = {
                    'count': len(values),
                    'average': np.mean([float(v) for v in values if str(v).isdigit()]) if any(str(v).isdigit() for v in values) else 0,
                    'distribution': Counter(values)
                }
        
        return {
            'total_participants': len(set(r.get('participant_id', r.get('record_id')) for r in self.data)),
            'utilization_stats': utilization_stats,
            'summary': self._summarize_utilization(utilization_stats)
        }
    
    def analyze_sleep_patterns(self):
        """Análise de padrões de sono"""
        if not self.data:
            return {'message': 'Nenhum dado disponível'}
        
        sleep_fields = [
            'sleep_quality', 'sleep_duration', 'sleep_disturbances',
            'bedtime', 'wake_time', 'sleep_efficiency'
        ]
        
        sleep_data = []
        for record in self.data:
            sleep_record = {}
            for field in sleep_fields:
                if field in record:
                    sleep_record[field] = record[field]
            if sleep_record:
                sleep_record['participant_id'] = record.get('participant_id', record.get('record_id'))
                sleep_data.append(sleep_record)
        
        analysis = {
            'total_sleep_records': len(sleep_data),
            'sleep_quality_stats': self._analyze_sleep_quality(sleep_data),
            'sleep_duration_stats': self._analyze_sleep_duration(sleep_data),
            'patterns': self._identify_sleep_patterns(sleep_data)
        }
        
        return analysis
    
    def analyze_medication_adherence(self):
        """Análise de adesão medicamentosa"""
        if not self.data:
            return {'message': 'Nenhum dado disponível'}
        
        medication_fields = [
            'medication_adherence', 'missed_doses', 'medication_changes',
            'side_effects', 'adherence_score', 'medication_count'
        ]
        
        adherence_data = []
        for record in self.data:
            med_record = {}
            for field in medication_fields:
                if field in record:
                    med_record[field] = record[field]
            if med_record:
                med_record['participant_id'] = record.get('participant_id', record.get('record_id'))
                adherence_data.append(med_record)
        
        analysis = {
            'total_medication_records': len(adherence_data),
            'adherence_stats': self._calculate_adherence_stats(adherence_data),
            'risk_factors': self._identify_adherence_risks(adherence_data),
            'recommendations': self._generate_adherence_recommendations(adherence_data)
        }
        
        return analysis
    
    def analyze_residence_comparison(self):
        """Análise de comparação por residência"""
        if not self.data:
            return {'message': 'Nenhum dados disponível'}
        
        residence_data = defaultdict(list)
        for record in self.data:
            residence = record.get('residence_type', record.get('location', 'unknown'))
            residence_data[residence].append(record)
        
        comparison = {}
        for residence, records in residence_data.items():
            comparison[residence] = {
                'participant_count': len(records),
                'health_metrics': self._calculate_residence_metrics(records),
                'demographics': self._analyze_residence_demographics(records)
            }
        
        return {
            'total_residences': len(residence_data),
            'comparison': comparison,
            'insights': self._generate_residence_insights(comparison)
        }
    
    def _get_date_range(self, records):
        """Obter range de datas dos registros"""
        dates = []
        for record in records:
            for key, value in record.items():
                if 'date' in key.lower() and value:
                    try:
                        date_obj = pd.to_datetime(value, errors='ignore')
                        if isinstance(date_obj, pd.Timestamp):
                            dates.append(date_obj)
                    except:
                        continue
        
        if dates:
            return {
                'start_date': min(dates).strftime('%Y-%m-%d'),
                'end_date': max(dates).strftime('%Y-%m-%d'),
                'duration_days': (max(dates) - min(dates)).days
            }
        return {'start_date': None, 'end_date': None, 'duration_days': 0}
    
    def _analyze_trends(self, records):
        """Analisar tendências nos registros"""
        trends = {}
        numeric_fields = []
        
        for record in records:
            for key, value in record.items():
                if isinstance(value, (int, float)) or (isinstance(value, str) and value.isdigit()):
                    numeric_fields.append(key)
        
        numeric_fields = list(set(numeric_fields))
        
        for field in numeric_fields[:5]:  # Limitar a 5 campos
            values = []
            for record in records:
                if field in record and record[field]:
                    try:
                        values.append(float(record[field]))
                    except:
                        continue
            
            if len(values) > 1:
                trends[field] = {
                    'trend': 'increasing' if values[-1] > values[0] else 'decreasing',
                    'change_percent': ((values[-1] - values[0]) / values[0] * 100) if values[0] != 0 else 0,
                    'values': values[:10]  # Últimos 10 valores
                }
        
        return trends
    
    def _summarize_utilization(self, stats):
        """Resumir estatísticas de utilização"""
        if not stats:
            return "Nenhum dado de utilização disponível"
        
        total_visits = sum(stat.get('count', 0) for stat in stats.values())
        most_common = max(stats.keys(), key=lambda k: stats[k].get('count', 0)) if stats else None
        
        return f"Total de {total_visits} utilizações registradas. Mais comum: {most_common}"
    
    def _analyze_sleep_quality(self, sleep_data):
        """Analisar qualidade do sono"""
        quality_scores = []
        for record in sleep_data:
            if 'sleep_quality' in record:
                try:
                    quality_scores.append(float(record['sleep_quality']))
                except:
                    continue
        
        if quality_scores:
            return {
                'average': np.mean(quality_scores),
                'median': np.median(quality_scores),
                'distribution': Counter([int(score) for score in quality_scores])
            }
        return {'average': 0, 'median': 0, 'distribution': {}}
    
    def _analyze_sleep_duration(self, sleep_data):
        """Analisar duração do sono"""
        durations = []
        for record in sleep_data:
            if 'sleep_duration' in record:
                try:
                    durations.append(float(record['sleep_duration']))
                except:
                    continue
        
        if durations:
            return {
                'average_hours': np.mean(durations),
                'recommended_range': (7, 9),
                'within_range_percent': len([d for d in durations if 7 <= d <= 9]) / len(durations) * 100
            }
        return {'average_hours': 0, 'recommended_range': (7, 9), 'within_range_percent': 0}
    
    def _identify_sleep_patterns(self, sleep_data):
        """Identificar padrões de sono"""
        patterns = {
            'consistent_bedtime': False,
            'regular_wake_time': False,
            'adequate_duration': False
        }
        
        # Lógica simplificada para identificar padrões
        if len(sleep_data) > 5:
            patterns['consistent_bedtime'] = True
            patterns['regular_wake_time'] = True
            patterns['adequate_duration'] = True
        
        return patterns
    
    def _calculate_adherence_stats(self, adherence_data):
        """Calcular estatísticas de adesão"""
        adherence_scores = []
        for record in adherence_data:
            if 'adherence_score' in record:
                try:
                    adherence_scores.append(float(record['adherence_score']))
                except:
                    continue
        
        if adherence_scores:
            return {
                'average_adherence': np.mean(adherence_scores),
                'high_adherence_percent': len([s for s in adherence_scores if s >= 80]) / len(adherence_scores) * 100,
                'low_adherence_count': len([s for s in adherence_scores if s < 50])
            }
        return {'average_adherence': 0, 'high_adherence_percent': 0, 'low_adherence_count': 0}
    
    def _identify_adherence_risks(self, adherence_data):
        """Identificar fatores de risco para não adesão"""
        risks = []
        
        missed_doses_count = len([r for r in adherence_data if r.get('missed_doses', 0) > 0])
        if missed_doses_count > 0:
            risks.append(f"{missed_doses_count} participantes com doses perdidas")
        
        side_effects_count = len([r for r in adherence_data if r.get('side_effects')])
        if side_effects_count > 0:
            risks.append(f"{side_effects_count} participantes relataram efeitos colaterais")
        
        return risks
    
    def _generate_adherence_recommendations(self, adherence_data):
        """Gerar recomendações para melhorar adesão"""
        recommendations = [
            "Implementar lembretes de medicação",
            "Monitoramento regular da adesão",
            "Educação sobre importância do tratamento"
        ]
        
        if len(adherence_data) > 0:
            low_adherence = len([r for r in adherence_data if r.get('adherence_score', 100) < 80])
            if low_adherence > 0:
                recommendations.append(f"Foco especial em {low_adherence} participantes com baixa adesão")
        
        return recommendations
    
    def _calculate_residence_metrics(self, records):
        """Calcular métricas por residência"""
        metrics = {
            'health_score_avg': 0,
            'satisfaction_avg': 0,
            'activity_level_avg': 0
        }
        
        # Lógica simplificada para calcular métricas
        health_scores = [r.get('health_score', 0) for r in records if r.get('health_score')]
        if health_scores:
            metrics['health_score_avg'] = np.mean(health_scores)
        
        return metrics
    
    def _analyze_residence_demographics(self, records):
        """Analisar demographics por residência"""
        ages = [r.get('age', 0) for r in records if r.get('age')]
        genders = [r.get('gender', 'unknown') for r in records if r.get('gender')]
        
        return {
            'average_age': np.mean(ages) if ages else 0,
            'gender_distribution': Counter(genders),
            'total_participants': len(records)
        }
    
    def _generate_residence_insights(self, comparison):
        """Gerar insights da comparação de residências"""
        insights = []
        
        if len(comparison) > 1:
            best_residence = max(comparison.keys(), 
                               key=lambda k: comparison[k].get('health_metrics', {}).get('health_score_avg', 0))
            insights.append(f"Melhor performance de saúde: {best_residence}")
            
            total_participants = sum(data.get('participant_count', 0) for data in comparison.values())
            insights.append(f"Total de {total_participants} participantes distribuídos entre {len(comparison)} residências")
        
        return insights
