import asyncio
from typing import Dict, Any, List
# from agents import get_classification_agent, get_task_creation_agent, get_task_execution_agent
from agents import get_task_execution_agent
# from services import get_message_pull_service
# from utils.logger import get_logger
from config.settings import settings


# logger = get_logger(__name__)


class Orchestrator:
    """
    Main orchestrator for the AI Multi-Agent System
    Coordinates message flow through classification, task creation, and execution
    """

    async def start(self):
        print("Starting AI Multi-Agent Orchestration System")
        message = {
            "message_id": '1',
            "title:": 'update Address',
            "content": 'HI, I want to update my new addres: 3 Broyer st. BB. thanks, malka blau.',
            "sender": 'malka.blau@sapiens.com',
            "channel": 'manual',
        }

        await self.process_message(message)

    def __init__(self):
        # self.classification_agent = get_classification_agent()
        # self.task_creation_agent = get_task_creation_agent()
        self.task_execution_agent = get_task_execution_agent()
        # self.message_service = get_message_pull_service()
        self.max_concurrent_tasks = settings.app.max_concurrent_tasks
        self.semaphore = asyncio.Semaphore(self.max_concurrent_tasks)

    async def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a single message through the full pipeline

        Args:
            message: Standardized message dictionary

        Returns:
            Processing result with status and response
        """
        async with (self.semaphore):
            try:
                print(f"Processing message {message.get('message_id')} from {message.get('channel')}")

                # Stage 1: Classification
                # classification_result = await self._classify_message(message)

                # if not classification_result:
                #   print("Classification failed")
                #    return self._create_error_result(message, "Classification failed")

                # Stage 2: Task Creation
                # task_data = await self._create_task(classification_result, message)

                # if not task_data:
                #   print("Task creation failed")
                #    return self._create_error_result(message, "Task creation failed")

                # Stage 3: Task Execution
                task_data = {
                    "execution_params": {
                        "api_endpoint": '/contact/28962',
                        "http_method": 'GET',
                        "timeout": 30
                    },
                    'ivo_json': {
                        "agent": "Noam Moatty 8 nnn nnn 1000 Israel",
                        "addresses": [
                            {
                                "zipCode": "1000",
                                "country": {
                                    "id": 99,
                                    "desc": "Israel"
                                },
                                "addressType": {
                                    "id": 1,
                                    "desc": "Private address"
                                },
                                "streetName": "nnn",
                                "cityName": "nnn",
                                "houseNr": "8345"
                            },
                            {
                                "zipCode": "7757424",
                                "country": {
                                    "id": 99,
                                    "desc": "Israel"
                                },
                                "addressType": {
                                    "id": 3,
                                    "desc": "Billing address"
                                },
                                "geoLongitude": 34.6529237,
                                "streetName": "HaKalanit",
                                "geoLatitude": 31.785414,
                                "cityName": "Ashdod",
                                "geoElevation": 28.271471,
                                "houseNr": "20"
                            }
                        ],
                        "subscriptions": [],
                        "onlinePlatformLinks": [],
                        "language": {
                            "id": 101,
                            "desc": "English - US"
                        },
                        "channelType": {
                            "id": 1,
                            "desc": "IDIT_UI"
                        },
                        "externalContactNumber": "28962",
                        "householdDescription": "Moatty - Sibony1 - Yelena - Collection date SLSA",
                        "entityType": {
                            "id": 1,
                            "desc": "Individual"
                        },
                        "contactBankAccount": [],
                        "firstName": "Noam",
                        "name": "Moatty",
                        "consents": [],
                        "gender": {
                            "id": 1,
                            "desc": "Female"
                        },
                        "telephones": [
                            {
                                "telephoneNumber": "321321",
                                "telephoneType": {
                                    "id": 1,
                                    "desc": "Private telephone"
                                },
                                "telephonePrefix": "010",
                                "countryDialCode": {
                                    "id": 1,
                                    "desc": "32"
                                }
                            }
                        ],
                        "contactRelationship": [
                            {
                                "relatedContactName": "Administrator",
                                "relationshipType": {
                                    "id": 43,
                                    "desc": "Client managed by"
                                },
                                "relatedContactID": 1,
                                "effectiveDate": "1990-01-01T00:00:00"
                            },
                            {
                                "relatedContactName": "Sharon Moatty",
                                "relationshipType": {
                                    "id": 15,
                                    "desc": "Family"
                                },
                                "relatedContactID": 28909,
                                "effectiveDate": "1990-01-01T00:00:00"
                            },
                            {
                                "relatedContactName": "Orit Sibony1",
                                "relationshipType": {
                                    "id": 15,
                                    "desc": "Family"
                                },
                                "discontinueDate": "2021-03-14T00:00:00",
                                "relatedContactID": 29084,
                                "effectiveDate": "1990-01-01T00:00:00",
                                "remarks": "test relationship"
                            },
                            {
                                "relatedContactName": "Moatty",
                                "relationshipType": {
                                    "id": 45,
                                    "desc": "Client of Intermediary"
                                },
                                "relatedContactID": 29086,
                                "effectiveDate": "1990-01-01T00:00:00"
                            },
                            {
                                "relatedContactName": "SHSHSH bbb Moatty",
                                "relationshipType": {
                                    "id": 5,
                                    "desc": "Daughter of Mother"
                                },
                                "relatedContactID": 35950,
                                "effectiveDate": "2013-12-18T10:13:34"
                            },
                            {
                                "relatedContactName": "Amitosh Moatty",
                                "relationshipType": {
                                    "id": 15,
                                    "desc": "Family"
                                },
                                "discontinueDate": "2013-01-07T00:00:00",
                                "relatedContactID": 35953,
                                "effectiveDate": "2011-12-21T00:00:00",
                                "remarks": "lead"
                            },
                            {
                                "relatedContactName": "Amitosh Moatty",
                                "relationshipType": {
                                    "id": 15,
                                    "desc": "Family"
                                },
                                "relatedContactID": 35953,
                                "effectiveDate": "2013-01-09T00:00:00"
                            },
                            {
                                "relatedContactName": "Yelena - Collection date SLSA",
                                "relationshipType": {
                                    "id": 15,
                                    "desc": "Family"
                                },
                                "relatedContactID": 38072,
                                "effectiveDate": "2014-08-27T00:00:00",
                                "remarks": "cccc"
                            }
                        ],
                        "preferredDeliveryType": {
                            "id": 3,
                            "desc": "Email"
                        },
                        "processingStatusVO": {
                            "id": 10000,
                            "desc": "Available for the processing"
                        },
                        "emails": [
                            {
                                "emailType": {
                                    "id": 10008,
                                    "desc": "Official"
                                },
                                "email": "sharon.moatty@sapiens111.com"
                            },
                            {
                                "emailType": {
                                    "id": 1,
                                    "desc": "Private"
                                },
                                "email": "test@ooooo.com"
                            }
                        ],
                        "demoPetObjects": [],
                        "accountManager": "Administrator",
                        "contactRole": [
                            {
                                "tContactRoleVO": {
                                    "id": 12,
                                    "desc": "Involved Party"
                                },
                                "effectiveDate": "1990-01-01T00:00:00"
                            },
                            {
                                "tContactRoleVO": {
                                    "id": 10024,
                                    "desc": "Intermediary Account Manager"
                                },
                                "effectiveDate": "2013-01-01T00:00:00"
                            },
                            {
                                "tContactRoleVO": {
                                    "id": 16,
                                    "desc": "Policyholder"
                                },
                                "effectiveDate": "2017-07-20T11:02:56"
                            },
                            {
                                "tContactRoleVO": {
                                    "id": 27,
                                    "desc": "Prospect"
                                },
                                "effectiveDate": "2019-05-29T10:59:29"
                            }
                        ],
                        "contactFormattedName": "Noam Moatty",
                        "identifiers": [],
                        "dateOfBirth": "1985-05-29T00:00:00",
                        "companyContacts": []

                    }
                }

                for key, value in task_data.items():
                    print(f"{key}:{value}")

                execution_result = await self._execute_task(task_data, message)

                # Stage 4: Send Response
                response_sent = await self._send_response(execution_result, message)

                # Compile final result
                result = {
                    "status": "success" if execution_result.get("execution_status") == "success" else "failed",
                    "message_id": message.get('message_id'),
                    "channel": message.get('channel'),
                    "classification": 'Update Contact',
                    "task": task_data,
                    "execution": execution_result,
                    "response_sent": response_sent
                }

                print(f"Message {message.get('message_id')} processed successfully")
                return result

            except Exception as e:
                print(f"Error processing message {message.get('message_id')}: {str(e)}")
                return {
                    "status": "error",
                    "message_id": message.get('message_id'),
                    "channel": message.get('channel'),
                    "error": e.__traceback__,
                    "classification": None,
                    "task": None,
                    "execution": None,
                    "response_sent": False
                }

    # n self._create_error_result(message, str(e))

    # async def process_messages(self, messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    #     """
    #     Process multiple messages concurrently
    #
    #     Args:
    #         messages: List of standardized messages
    #
    #     Returns:
    #         List of processing results
    #     """
    #     print(f"Processing {len(messages)} messages")
    #
    #     tasks = [self.process_message(msg) for msg in messages]
    #     results = await asyncio.gather(*tasks, return_exceptions=True)
    #
    #     # Handle any exceptions
    #     processed_results = []
    #     for idx, result in enumerate(results):
    #         if isinstance(result, Exception):
    #             print(f"Error processing message {idx}: {str(result)}")
    #             processed_results.append(self._create_error_result(messages[idx], str(result)))
    #     else:
    #         processed_results.append(result)
    #
    #     return processed_results

    async def _execute_task(self, task_data: Dict[str, Any], message: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task via IDIT API"""
        try:
            print(f"Executing task {task_data.get('task_id')}")

            execution_result = await self.task_execution_agent.execute_task(task_data, message)

            return execution_result

        except Exception as e:
            print(f"Task execution error: {str(e)}")
            return {
                "execution_status": "failed",
                "error": str(e),
                "user_response": "An error occurred while processing your request."
            }

    async def _send_response(self, execution_result: Dict[str, Any], message: Dict[str, Any]) -> bool:
        """Send response back to user via appropriate channel"""
        try:
            channel = message.get('channel')
            sender = message.get('sender')
            response_text = execution_result.get('user_response', 'Your request has been processed.')

            # Prepare metadata based on channel
            metadata = {}
            if channel == 'email':
                original_subject = message.get('metadata', {}).get('subject', '')
                metadata['subject'] = f"Re: {original_subject}" if original_subject else "Response to your inquiry"
            elif channel == 'teams':
                metadata['title'] = "Task Update"
                metadata['type'] = 'success' if execution_result.get('execution_status') == 'success' else 'error'

            # # Send response
            # success = await self.message_service.send_response(
            #     channel=channel,
            #     recipient=sender,
            #     content=response_text,
            #     metadata=metadata
            # )
            success = bool()

            if success:
                print(f"Response sent successfully to {sender} via {channel}")
            else:
                print(f"Failed to send response to {sender} via {channel}")

            return success

        except Exception as e:
            print(f"Error sending response: {str(e)}")
            return False

    #
    #
    # def _create_error_result(self, message: Dict[str, Any], error: str) -> Dict[str, Any]:
    #     """Create error result"""
    #     return {
    #         "status": "error",
    #         "message_id": message.get('message_id'),
    #         "channel": message.get('channel'),
    #         "error": error,
    #         "classification": None,
    #         "task": None,
    #         "execution": None,
    #         "response_sent": False
    #     }
    #
    #

    def stop(self):
        """Stop the orchestrator"""
        print("Stopping AI Multi-Agent Orchestration System")
        # self.message_service.stop_polling()

    #
    # async def start(self):
    #     """Start the orchestrator in polling mode"""
    #     print("Starting AI Multi-Agent Orchestration System")
    #
    #     try:
    #         # Start message polling with callback
    #         await self.message_service.start_polling(self.process_messages)
    #
    #     except KeyboardInterrupt:
    #         print("Received shutdown signal")
    #         self.stop()
    #     except Exception as e:
    #         print(f"Orchestrator error: {str(e)}")
    #         raise
    #
    #
    # async def _classify_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
    #     """Run message through classification agent"""
    #     try:
    #         print(f"Classifying message {message.get('message_id')}")
    #
    #         # Run classification in executor to avoid blocking
    #         loop = asyncio.get_event_loop()
    #         classification = await loop.run_in_executor(
    #             None,
    #             self.classification_agent.classify_message,
    #             message
    #         )
    #
    #         return classification
    #
    #     except Exception as e:
    #         print(f"Classification error: {str(e)}")
    #         return None
    #
    #
    # async def _create_task(self, classification: Dict[str, Any], message: Dict[str, Any]) -> Dict[str, Any]:
    #     """Create task from classification result"""
    #     try:
    #         print(f"Creating task for action_id: {classification.get('action_id')}")
    #
    #         # Run task creation in executor
    #         loop = asyncio.get_event_loop()
    #         task_data = await loop.run_in_executor(
    #             None,
    #             self.task_creation_agent.create_task,
    #             classification,
    #             message
    #         )
    #
    #         return task_data
    #
    #     except Exception as e:
    #         print(f"Task creation error: {str(e)}")
    #         return None

    # Singleton instance


_orchestrator = None


def get_orchestrator() -> Orchestrator:
    """Get or create orchestrator singleton"""
    print("getting orchestrator...")
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = Orchestrator()
    return _orchestrator
