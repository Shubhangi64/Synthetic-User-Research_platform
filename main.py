import argparse, json
from src.ai_client import test_connection
from src.config import SCENARIOS
from src.experiment import load_personas,get_scenario
from src.personas import generate_to_target,print_personas
from src.survey import run_survey,display_side_by_side
from src.validation import run_validation,print_validation_summary
from src.insights import calculate_scores,deterministic_insights
from src.service import run_research

def main():
    p=argparse.ArgumentParser(description='Synthetic User Research Platform')
    p.add_argument('--test',action='store_true'); p.add_argument('--generate-personas',type=int); p.add_argument('--show-personas',action='store_true'); p.add_argument('--survey',action='store_true'); p.add_argument('--validate',action='store_true'); p.add_argument('--insights',action='store_true'); p.add_argument('--demo',action='store_true'); p.add_argument('--scenario',choices=list(SCENARIOS),default='shopping')
    a=p.parse_args(); people=load_personas()
    if a.test: print('LLM/provider available.' if test_connection() else 'LLM/provider is not available.'); return
    if a.generate_personas: print_personas(generate_to_target(a.generate_personas)); return
    if a.show_personas: print_personas(people[:10]); return
    if a.survey:
        r=run_survey(people[:5],get_scenario(a.scenario)); display_side_by_side(r,get_scenario(a.scenario)['questions']); return
    if a.validate:
        saved=json.loads(open('results/survey_results.json',encoding='utf-8').read()); print_validation_summary(run_validation(people[:len(saved['responses'])],saved['responses'])); return
    if a.insights:
        saved=json.loads(open('results/survey_results.json',encoding='utf-8').read()); print(json.dumps(deterministic_insights(saved['experiment'],saved['responses']),indent=2)); return
    if a.demo:
        state=run_research(get_scenario(a.scenario),get_scenario(a.scenario)['questions'],people[:5],True,True); print(json.dumps({'run_id':state['run_id'],'would_use_product':state['would_use_product'],'evaluation':state.get('evaluation',{}),'insights':state.get('insights',{})},indent=2)); return
    p.print_help()
if __name__=='__main__': main()
