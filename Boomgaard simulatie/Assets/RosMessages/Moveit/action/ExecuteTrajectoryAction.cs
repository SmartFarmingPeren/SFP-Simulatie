using System.Collections.Generic;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;


namespace RosMessageTypes.Moveit
{
    public class ExecuteTrajectoryAction : Action<ExecuteTrajectoryActionGoal, ExecuteTrajectoryActionResult, ExecuteTrajectoryActionFeedback, ExecuteTrajectoryGoal, ExecuteTrajectoryResult, ExecuteTrajectoryFeedback>
    {
        public const string RosMessageName = "moveit_msgs/ExecuteTrajectoryAction";

        public ExecuteTrajectoryAction() : base()
        {
            this.action_goal = new ExecuteTrajectoryActionGoal();
            this.action_result = new ExecuteTrajectoryActionResult();
            this.action_feedback = new ExecuteTrajectoryActionFeedback();
        }

        public override List<byte[]> SerializationStatements()
        {
            var listOfSerializations = new List<byte[]>();
            listOfSerializations.AddRange(this.action_goal.SerializationStatements());
            listOfSerializations.AddRange(this.action_result.SerializationStatements());
            listOfSerializations.AddRange(this.action_feedback.SerializationStatements());

            return listOfSerializations;
        }

        public override int Deserialize(byte[] data, int offset)
        {
            offset = this.action_goal.Deserialize(data, offset);
            offset = this.action_result.Deserialize(data, offset);
            offset = this.action_feedback.Deserialize(data, offset);

            return offset;
        }

    }
}
